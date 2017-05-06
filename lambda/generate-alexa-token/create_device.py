import sys
import logging
import rds_config
import pymysql
import constants
import random
import string
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

    result = 0

    success = False
    
    token = ""

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `client_account` WHERE `username` = \"{0}\";".format(user_name))
        result = cursor.fetchall()
        if len(result) == 1:
            success = pbkdf2_sha256.verify(user_password, result[0][constants.PWD_KEY_INDEX])
            if success:
                user_id = result[0][constants.ID_INDEX]
                token = str(user_id) + "".join(random.choices(string.ascii_letters + string.digits, k = 501))
                cursor.execute("UPDATE `client_device`" +
                               " SET `alexa_token` = \"{0}\" WHERE `id` = {1}".format(token, user_id))
    
        conn.commit()
        conn.close()
        return ({
            'token' = token
        })
        