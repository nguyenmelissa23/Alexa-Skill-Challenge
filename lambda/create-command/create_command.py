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

    alexa_token = event['token']
    if alexa_token == 0 or alexa_token == "":
        return False

    device_alias = event['device']
    repo_alias = event['repository']

    command_id = event['command']
    command_extra = event['extra']

    result = 0

    success = False
    
    token = ""

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `client_account` WHERE `alexa_token` = \"{0}\";".format(alexa_token))
        result = cursor.fetchall()
        if len(result) == 1:
            user_id = result[0][constants.ID_INDEX]
            cursor.execute("SELECT * FROM `client_device` WHERE `user_id` = \"{0}\" AND `alias` = \"{1}\" ;".format(user_id, device_alias))
            result = cursor.fetchall()
            if len(result) == 1:
                device_id = result[0][constants.ID_INDEX]
                cursor.execute("SELECT * FROM `client_device` WHERE `device_id` = \"{0}\" AND `alias` = \"{1}\" ;".format(device_id, repo_alias))
                if len(result) == 1:
                    repo_id = result[0][constants.ID_INDEX]
                    cursor.execute("INSERT INTO `device_command`(`device_id`, `repo_id`, `command_id`, `command_extra`)" +
                                   " VALUES(\"{0}\", \"{1}\", \"{2}\", \"{3}\");".format(device_id, repo_id, command_id, command_extra))
    
        conn.commit()
        conn.close()
        return(success)
        