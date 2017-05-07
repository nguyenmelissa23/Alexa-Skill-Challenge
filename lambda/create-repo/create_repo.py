import sys
import logging
import rds_config
import pymysql
import constants
import random
import string

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

    device_token = event['token']
    
    repo_path = event['path']
    repo_alias = event['alias']

    result = 0
    
    success = False

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `client_device` WHERE `device_token` = \"{0}\";".format(device_token))
        result = cursor.fetchall()
        if len(result) == 1:
            device_id = result[0][constants.ID_INDEX]
            cursor.execute("INSERT INTO `user_repository`(`device_id`, `alias`, `path`)" +
                           " VALUES(\"{0}\", \"{1}\", \"{2}\");".format(device_id, repo_alias, repo_path))
            success = True

        conn.commit()
        conn.close()
        return success
        