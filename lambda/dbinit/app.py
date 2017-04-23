import sys
import logging
import rds_config
import pymysql
#rds settings
rds_host  = "gitwachdb.c0tsrytvgqif.us-west-1.rds.amazonaws.com"
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name


logger = logging.getLogger()
logger.setLevel(logging.INFO)

try:
    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
except:
    logger.error("ERROR: Unexpected error: Could not connect to MySql instance.")
    sys.exit()

logger.info("SUCCESS: Connection to RDS mysql instance succeeded")
def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    item_count = 0

    with conn.cursor() as cur:
        #cur.execute("create table Employee3 ( EmpID  int NOT NULL, Name varchar(255) NOT NULL, PRIMARY KEY (EmpID))") 
        cur.execute("""CREATE TABLE `client_account`(
	                    `id` INT(11) auto_increment NOT NULL,
	                    `username` VARCHAR(256) NOT NULL,
                        `pwd_key` VARCHAR(256) NOT NULL, 
                        `token` VARCHAR(512) NOT NULL,
                           PRIMARY KEY (`id`)); )""" )
        conn.commit()
        cur.execute("select * from Employee3")
        for row in cur:
            item_count += 1
            logger.info(row)
            #print(row)
    

    print( "Added %d items from RDS MySQL table" %(item_count))