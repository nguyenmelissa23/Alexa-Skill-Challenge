import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = rds_config.db_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name


logger = logging.getLogger()
logger.setLevel(logging.INFO)


conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=30, port=3306)

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        #cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))") 
        cur.execute("INSERT into `client_account`( `username`, `pwd_key`)" +
                       " VALUES ( \"Xpression\", \"password\")")
        conn.commit()
        conn.close()
        return "Inserted user"
        