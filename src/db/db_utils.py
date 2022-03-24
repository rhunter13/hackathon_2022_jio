import enum

from werkzeug.exceptions import HTTPException
from logging import getLogger
from pymysql import Binary
from sqlalchemy import (
    LargeBinary,
    MetaData,
    String,
    Column,
    Table,
    Boolean,
    Text,
    create_engine,
    insert
)

from src.commons.settings import MYSQL_CONNECTION_STRING

logger = getLogger()
class TableNames(enum.Enum):
    login = "login"
    user_details = "user_details"


def get_login_table(table_name,meta):
    table = Table(
        table_name,
        meta,
        Column("username",String(100),primary_key=True,index=True),
        Column("password", String(100))
    )
    return table

def get_user_details(table_name,meta):
    table = Table(
        table_name,
        meta,
        Column("username",String(100),primary_key=True,index=True),
        Column("primary_cont",String(100)),
        Column("secondary_cont",String(100)),
        Column("primary_cont_num",String(10)),
        Column("secondary_cont_num",String(10)),
        Column("bp_value",String(50)),
        Column("diabetes",String(10)),
        Column("health_condition",Text)
    )
    return table

class DatabaseConnection():
    def __init__(self,mysql_connection_string=None,logger=logger):
        self.logger = logger
        if not mysql_connection_string:
            mysql_connection_string = MYSQL_CONNECTION_STRING
        engine = create_engine(mysql_connection_string)
        self.engine = engine
        meta = MetaData()
        self.login_table = get_login_table(TableNames.login.value,meta)
        self.user_details_table = get_user_details(TableNames.user_details.value,meta)
        meta.create_all(engine)

        self.table_map={
            TableNames.login.value : self.login_table,
            TableNames.user_details.value : self.user_details_table
        }

    def get_table_from_name(self,name):
        return self.table_map.get(name)

    def add_data_into_table(self,data,table_name):
        self.logger.debug({"data":data, "table_name":table_name})
        table = self.get_table_from_name(table_name)
        query = insert(table).values(data)
        connection = self.engine.connect()
        try:
            executed_data = connection.execute(query)
            self.logger.debug("executed data %s", executed_data)
            connection.close()
            return executed_data
        except Exception as e:
            self.logger.exception(f"function name add_data_into_table : Exception {e}")
            self.logger.debug(f"data: {data}")
            raise HTTPException(status_code=400, detail="duplicate data found in the database")
        finally:
            connection.close()
        
    def get_result_from_query(self,query):
        try:
            connection = self.engine.connect()
            result = connection.execute(query)
            rows = result.fetchall()
            connection.close()
            return rows
        except Exception as e:
            self.logger.exception(f"function name get_result_from_query : Exception {e}")
            self.logger.debug(f"query: {query}")
        finally:
            if connection in locals():
                connection.close()