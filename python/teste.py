import logging
from psycopg2 import connect
logger=logging.getLogger()
logger.setLevel(logging.info)


class Database:
    def __init__(self):
        db_name="teste"
        db_user="postgres"
        db_password="110102ee"
        db_host="localhost"
        db_port="5432"
        
        try:
            conn=connect(
            host=db_host,
            user=db_user,
            dbname=db_name,
            password=db_password,
            port=db_port
            )
        except Exception as error:
            print(error)
        
        logger.info("Database connection suceed")
        self.__connection=conn
        
        
    def insert(self,query):
        cursor=self.__connection.cursor()
        sql_query=f"INSERT INTO {query}"
        try:
            cursor.execute(sql_query)
            self.__connection.commit()
        except Exception as error:
            self.__connection.rollback()
            print(error)
        finally:
            cursor.close()
            self.__connection.close()
    
    def delete(self,query):
        cursor=self.__connection.cursor()
        sql_query=f"DELETE FROM {query}"
        try:
            cursor.execute(sql_query)
            self.__connection.commit()
        except Exception as error:
            self.__connection.rollback()
            print(error)
        finally:
            cursor.close()
            self.__connection.close()
            
    def update(self,query):
        cursor=self.__connection.cursor()