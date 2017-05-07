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

    alexa_token = event['token']
    if alexa_token == 0 or alexa_token == "":
        return False

    result = 0
    repositories = {}

    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM `client_account` WHERE `token` = \"{0}\";".format(alexa_token))
        result = cursor.fetchall()
        if len(result) == 1:
            user_id = result[0][constants.ID_INDEX]
            cursor.execute("SELECT `client_device`.`alias`, `user_repository`.`alias` FROM `client_account` " +
                " INNER JOIN `client_device` ON `client_device`.`user_id` = `client_account`.`id`" +
                " INNER JOIN `user_repository` ON `user_repository`.`device_id` = `client_device`.`id`" +
                " WHERE `client_device`.`user_id` = \"{0}\";".format(user_id))
            result = cursor.fetchall()
            for repo in result:
                if repo[constants.DEVICE_ALIAS_INDEX] in repositories:
                    repositories[repo[constants.DEVICE_ALIAS_INDEX]].append(repo[constants.REPO_ALIAS_INDEX])
                else:
                    repositories[repo[constants.DEVICE_ALIAS_INDEX]] = [ repo[constants.REPO_ALIAS_INDEX] ]
    
        conn.commit()
        conn.close()
        return(repositories)
        