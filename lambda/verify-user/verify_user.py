import sys
import logging
import rds_config
import pymysql

#rds settings
rds_host  = rds_config.db_host
name = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

def handler(event, context):
    """
    This function fetches content from mysql RDS instance
    """

    conn = pymysql.connect(rds_host, user=name, passwd=password, db=db_name, connect_timeout=30, port=3306)

    user_name = event['username']
    
    result = 0

    success = False

    #pbkdf2_sha256.verify(password, hash)
    with conn.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM `client_account` WHERE `username` = \"{0}\";".format(user_name))    
        result = cursor.fetchall()
        if result[0][0] == 0:
            success = False
        else:
            success = True
    
        conn.commit()
        conn.close()
        return({ "exists": success })
        