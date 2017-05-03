import sys
import logging
import rds_config
import pymysql
from passlib.hash import pbkdf2_sha256

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
    user_password = event['password']
    device_alias = event['alias']

    result = 0

    success = False

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `client_account` WHERE `username` = \"{0}\";".format(user_name))    
        result = cursor.fetchall()
        if len(result == 1):
            success = pbkdf2_sha256.verify(password, result[0]["pwd_key"])
            if success:
                user_id = result[0]['id']
                token = str(user_id) + random.choices(string.ascii_letters + string.digits, k = 501)
                cursor.execute("INSERT INTO `client_devices`(`user_id`, `device_token`, `alias`)" +
                               " VALUES(\"{0}\", \"{1}\", \"{2}\");".format(user_id, token, device_alias))
                return token
    
        conn.commit()
        conn.close()
        return("")
        