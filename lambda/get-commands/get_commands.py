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

    device_token = event['token']

    result = 0
    commandlist = []

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `client_device` WHERE `token` = \"{0}\";".format(device_token))
        result = cursor.fetchall()
        if len(result) == 1:
            device_id = result[0][constants.ID_INDEX]
            cursor.execute("SELECT `device_commands`.`command_id`, `device_commands`.`command_extra`, `user_repository`.`path`" +
                           " FROM `device_commands` " +
                           " WHERE `device_id` = \"{0}\"" .format(device_id)) +
                           " INNER JOIN `user_repository` ON `device_commands`.`repo_id` = `user_repository`.`id`);")
            
            result = cursor.fetchall()
            for command in result:
                commandlist.append({
                    'command_id' : command[constants.COMMAND_ID_INDEX],
                    'command_extra' : command[constants.COMMAND_EXTRA_INDEX],
                    'path' : command[COMMAND_PATH_INDEX]
                })
        else:
            result = []
        conn.commit()
        conn.close()
        return [commandlist]