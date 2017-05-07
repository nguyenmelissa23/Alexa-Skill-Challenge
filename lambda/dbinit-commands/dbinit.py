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

    with conn.cursor() as cur:        
        cur.execute("CREATE TABLE `device_command`("
                       " `id` INT(11) auto_increment NOT NULL,"
                       " `device_id` INT(11) NOT NULL,"
                       " `repo_id` INT(11) NOT NULL,"
                       " `command_id` INT(11) NOT NULL,"
                       " `command_extra` VARCHAR(256),"
                       " PRIMARY KEY (`id`),"
                       " FOREIGN KEY (`device_id`) REFERENCES `client_device` (`id`),"
                       " FOREIGN KEY (`repo_id`) REFERENCES `user_repository` (`id`));" )
        conn.commit()
        conn.close()
        return "Created table"