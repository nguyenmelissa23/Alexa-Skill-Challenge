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
        cur.execute("CREATE TABLE `user_repository`("
                       " `id` INT(11) auto_increment NOT NULL,"
                       " `device_id` INT(11) NOT NULL,"
                       " `alias` VARCHAR(256) NOT NULL,"
                       " `path` VARCHAR(512) NOT NULL,"
                       " PRIMARY KEY (`id`),"
                       " FOREIGN KEY (`device_id`) REFERENCES `client_device` (`id`));" )
        conn.commit()
        conn.close()
        return "Created table"