import os
import mysql.connector

class SQL_Module:
    def __init__(self):
        # db_host = os.environ.get('DB_HOST')
        # db_user = os.environ.get('DB_USER')
        # db_password = os.environ.get('DB_PASSWORD')
        # db_name = os.environ.get('DB_NAME')
        # db = mysql.connector.connect(host=db_host,
        #                          user=db_user,
        #                          password=db_password,
        #                          database=db_name)
        pass

    def checkTableExists(self, dbcon, tablename):
        dbcur = dbcon.cursor()
        dbcur.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if dbcur.fetchone()[0] == 1:
            dbcur.close()
            return True

        dbcur.close()
        return False

    def extractDataFromURL(self, url:str):
        temp_list = url.split('/')
        brand = temp_list[4] #table name
        print(brand)

sql = SQL_Module()
sql.extractDataFromURL('https://www.otomoto.pl/oferta/bmw-seria-5-piekne-rodzinne-bmw-520d-ID6Ei1VH.html')