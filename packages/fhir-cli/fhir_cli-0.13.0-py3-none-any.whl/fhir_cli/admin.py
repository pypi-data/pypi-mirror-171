import getpass
import glob
import re
from pathlib import Path
from typing import Iterator
from uuid import NAMESPACE_URL, uuid5

import requests
from psycopg2 import connect, sql

from fhir_cli import (
    CONNECT_URL,
    DBT_META_TABLE,
    DBT_SCHEMA,
    FHIR_DBT_SCHEMA,
    FUNCTIONS_DIR_NAME,
    INIT_DB_TEMPLATE,
    JINJA_ENV,
    OMOP_DBT_SCHEMA,
    OMOP_TEMPLATES,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_SERVER_NAME,
    POSTGRES_SOURCE_CONNECTOR_TEMPLATE,
    POSTGRES_USER,
    log,
)


class InvalidJDBCUrlError(ValueError):
    pass


def get_user_defined_functions() -> Iterator[str]:
    """Yield SQL functions from the functions folder

    Returns:
        Iterator[str]: the SQL functions
    Raises:
        FileNotFoundError: if the function folder does not exist on the current path
    """
    if not Path(FUNCTIONS_DIR_NAME).is_dir():
        raise FileNotFoundError(f"{FUNCTIONS_DIR_NAME} folder not found")
    for file_path in glob.iglob(f"{FUNCTIONS_DIR_NAME}/**/*.sql", recursive=True):
        with open(file_path, "r") as f:
            yield f.read()


def db_type_from(url: str) -> str:
    """Extract the database type from the provided JDBC connection url

    Returns:
        str: the database type which can be either oracle or postgres
    Raises:
        InvalidJDBCUrlError: if the JDBC url is invalid
    """
    if (m := re.match(r"^jdbc:(postgres|oracle)://.+:\d+/\w+$", url)) is not None:
        return m.group(1)
    raise InvalidJDBCUrlError(f"JDBC url: {url} is invalid")


class Admin:
    """The admin command is used by an administrator to initialize a new project"""

    @staticmethod
    def createdb(database: str):
        """Create a new db for the project

        Args:
            database (str): a name for the new database
        """

        conn = connect(
            host=POSTGRES_HOST,
            dbname=POSTGRES_DB,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )
        conn.autocommit = True

        stmt = sql.SQL("CREATE DATABASE {database}").format(database=sql.Identifier(database))

        try:
            with conn.cursor() as curs:
                curs.execute(stmt)
        except Exception as e:
            log.error(e)
        finally:
            conn.close()

    @staticmethod
    def initdb(database: str, url: str, user: str = None, password: str = None, omop=False):
        """Initialize the new db for the project

        The omop vocabulary tables are populated during this process. It may take some time.

        Args:
            database (str): the database to initialize
            url (str): the source database JDBC url (formatted \
as jdbc:database_type//host:port/dbname) used to generate the project id
            user (:obj:`str`, optional): a username of choice.
            password (:obj:`str`, optional): a password of choice. If not specified, \
the command will prompt for a password
            omop (:obj:`bool`, optional): If specified, The omop vocabulary tables will be \
            populated during this process. It may take some time.
        """

        try:
            db_type = db_type_from(url)
        except InvalidJDBCUrlError as e:
            log.error(e)
            return

        while not password:
            password = getpass.getpass()

        conn = connect(
            host=POSTGRES_HOST,
            dbname=database,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )

        user_stmt = sql.SQL("CREATE USER {role} WITH PASSWORD %s").format(role=sql.Identifier(user))

        project_id = uuid5(NAMESPACE_URL, url)
        initdb_stmt = JINJA_ENV.get_template(INIT_DB_TEMPLATE).render(
            database=database,
            db_type=db_type,
            dbt_schema=DBT_SCHEMA,
            dbt_meta_table=DBT_META_TABLE,
            project_id=project_id,
            role=user,
            project_url=url,
        )

        try:
            with conn:
                with conn.cursor() as curs:
                    log.info("Creating a new user...")
                    curs.execute(user_stmt, (password,))
                    log.info("Initializing the project database...")
                    curs.execute(initdb_stmt)
                    if omop:
                        log.info("Loading OMOP vocabulary tables...")
                        for template in OMOP_TEMPLATES:
                            omop_stmt = JINJA_ENV.get_template(template).render(
                                schema=OMOP_DBT_SCHEMA
                            )
                            curs.execute(omop_stmt)
                    set_search_path_stmt = sql.SQL("SET search_path TO {dbt_schema}").format(
                        dbt_schema=sql.Identifier(DBT_SCHEMA)
                    )
                    curs.execute(set_search_path_stmt)
                    log.info("Loading user defined functions...")
                    for func_definition in get_user_defined_functions():
                        curs.execute(func_definition)
        except Exception as e:
            log.error(e)
        finally:
            conn.close()

    @staticmethod
    def add_omop_vocab(database: str):
        """Add omop vocabulary tables

        Args:
            database (str): the target database
        """
        conn = connect(
            host=POSTGRES_HOST,
            dbname=database,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )

        try:
            with conn:
                with conn.cursor() as curs:
                    log.info("Loading OMOP vocabulary tables...")
                    for template in OMOP_TEMPLATES:
                        omop_stmt = JINJA_ENV.get_template(template).render(schema=OMOP_DBT_SCHEMA)
                        curs.execute(omop_stmt)
        except Exception as e:
            log.error(e)
        finally:
            conn.close()

    @staticmethod
    def connect(database: str):
        """Add a Kafka Connect connector

        Args:
            database (str): the database to connect
        """
        source_connector = JINJA_ENV.get_template(POSTGRES_SOURCE_CONNECTOR_TEMPLATE).render(
            project_db=database,
            postgres_server_name=POSTGRES_SERVER_NAME,
            postgres_port=POSTGRES_PORT,
            postgres_user=POSTGRES_USER,
            postgres_password=POSTGRES_PASSWORD,
            fhir_schema=FHIR_DBT_SCHEMA,
        )
        r = requests.post(
            f"{CONNECT_URL}/connectors/",
            data=source_connector,
            headers={"Content-Type": "application/json"},
        )
        r.raise_for_status()

    @staticmethod
    def dblink(
        target: str, source: str, type: str, host: str, port: int, user: str, password: str = None
    ):
        """Create a foreign server linking the source database to the project database

        This command uses a foreign data wrapper to create a connection to another database
        thanks to the provided credentials.

        Args:
            target (str): the target database
            source (str): the source database
            type (str): the source database type (can be either `oracle`, `postgres` or `tds`)
            host (str): the source server host
            port (int): the source server port
            user (str): a source database user
            password (str): the user password. If not specified, the command will prompt for a
            password. If the password contains a special character, make sure you escape it properly
            `--password '"double#escape"'
        """

        while not password:
            password = getpass.getpass()

        conn = connect(
            host=POSTGRES_HOST,
            dbname=target,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )

        stmt = JINJA_ENV.get_template(f"{type}_fdw.sql.j2").render(
            source_db=source,
            source_host=host,
            source_port=port,
            source_user=user,
            source_password=password,
        )

        try:
            with conn:
                with conn.cursor() as curs:
                    curs.execute(stmt)
        except Exception as e:
            log.error(e)
        finally:
            conn.close()
