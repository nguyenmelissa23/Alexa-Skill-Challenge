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
#except:
#    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
#    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        cur.execute("CREATE TABLE `client_account`( "
	                   " `id` INT(11) auto_increment NOT NULL,"
	                   " `username` VARCHAR(256) NOT NULL,"
                       " `pwd_key` VARCHAR(256) NOT NULL," 
                       " `alexa_token` VARCHAR(512) NOT NULL DEFAULT \"0\","
                       " PRIMARY KEY (`id`));" )
        conn.commit()
        conn.close()
        return "Created table"