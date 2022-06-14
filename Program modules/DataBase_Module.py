from os import environ
import mysql.connector

class SQL_Module:
    def __init__(self, url, car_dict):
        db_host = environ.get('DB_HOST')
        db_user = environ.get('DB_USER')
        db_password = environ.get('DB_PASSWORD')
        print(db_user, db_password, db_host)
        self.db = mysql.connector.connect(host=db_host,
                                    user=db_user,
                                    password=db_password,
                                    )
        self.url = url
        self.car_dict = car_dict

    def create_table(self):
        dbcursor = self.db.cursor()
        brand = self.extractDataFromURL(self.url)
        if self.checkTableExists(brand) is False:
            dbcursor.execute(
                f"""CREATE TABLE `otomotoprogram`.`{brand}` (
                  `id` INT NOT NULL,
                  `url` LONGTEXT NOT NULL,
                  `price` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`id`));""")
        else:
            print(f"there is a table like {brand}")

        for url, prize in self.car_dict:
            dbcursor.execute(f"""INSERT INTO {brand} (car, price) values ({url},{prize})""")

    def checkTableExists(self, tablename):
        dbcursor = self.db.cursor()
        dbcursor.execute("""
            SELECT COUNT(*)
            FROM information_schema.tables
            WHERE table_name = '{0}'
            """.format(tablename.replace('\'', '\'\'')))
        if dbcursor.fetchone()[0] == 1:
            dbcursor.close()
            return True

        dbcursor.close()
        return False

    def extractDataFromURL(self, url:str):
        temp_list = url.split('/')
        brand = temp_list[4].split('-')[0] #table name
        print(brand)
        return brand

# url = 'https://www.otomoto.pl/oferta/bmw-seria-5-piekne-rodzinne-bmw-520d-ID6Ei1VH.html'
# sql = SQL_Module(url)
# sql.create_table()