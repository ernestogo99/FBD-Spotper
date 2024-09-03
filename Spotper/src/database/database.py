# pylint: disable=all
import logging
from psycopg2 import connect, OperationalError

# Configuração do logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class DatabaseService:
    def __init__(self):
        db_name = "teste"
        db_user = "postgres"
        db_password = "110102ee"
        db_host = "localhost"
        db_port = "5432"
        
        try:
            self.__connection = connect(
                host=db_host,
                user=db_user,
                dbname=db_name,
                password=db_password,
                port=db_port
            )
            logger.info("Database connection succeed")
        except OperationalError as error:
            logger.error(f"Error connecting to the database: {error}")
            self.__connection = None

    def insert(self, query, params=None):
        if self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute(query, params)
                self.__connection.commit()
            except Exception as error:
                self.__connection.rollback()
                logger.error(f"Error executing insert: {error}")
            finally:
                cursor.close()

    def delete(self, query, params=None):
        if self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute(query, params)
                self.__connection.commit()
            except Exception as error:
                self.__connection.rollback()
                logger.error(f"Error executing delete: {error}")
            finally:
                cursor.close()

    def update(self, query, params=None):
        if self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute(query, params)
                self.__connection.commit()
            except Exception as error:
                self.__connection.rollback()
                logger.error(f"Error executing update: {error}")
            finally:
                cursor.close()

    def search(self, query, params=None):
        rows = []
        if self.__connection:
            cursor = self.__connection.cursor()
            try:
                cursor.execute(query, params)
                rows = cursor.fetchall()
            except Exception as error:
                self.__connection.rollback()
                logger.error(f"Error executing search: {error}")
            finally:
                cursor.close()
        return rows

    def close_connection(self):
        if self.__connection:
            self.__connection.close()
            logger.info("Database connection closed")
