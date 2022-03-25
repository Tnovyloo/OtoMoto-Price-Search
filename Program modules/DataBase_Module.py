import os
import mysql.connector

class SQL_Module:
    def __init__(self):
        db_host = os.environ.get('DB_HOST')
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_name = os.environ.get('DB_NAME')
        db = mysql.connector.connect(host=db_host,
                                 user=db_user,
                                 password=db_password,
                                 database=db_name)

