from os import environ
import mysql.connector

class SQL_Module:
    def __init__(self, url, car_dict, actual_currency):
        db_host = environ.get('DB_HOST')
        db_user = environ.get('DB_USER')
        db_password = environ.get('DB_PASSWORD')
        # print(db_user, db_password, db_host)
        self.db = mysql.connector.connect(host=db_host,
                                    user=db_user,
                                    password=db_password,
                                    )
        self.url = url
        self.car_dict = car_dict
        self.actual_currency = actual_currency

    def start(self):
        dbcursor = self.db.cursor()
        dbcursor.execute("USE otomotoprogram;")

        # for car in self.car_dict.items():
        #     brand = self.extractDataFromURL(car[1])
        #     if self.checkTableExists(brand) is False: #Create table if brand table doesnt exist
        #         dbcursor.execute(
        #             f"""CREATE TABLE `otomotoprogram`.`{brand}` (
        #                               `id` INT NOT NULL AUTO_INCREMENT,
        #                               `url` LONGTEXT NOT NULL,
        #                               `price` INT NOT NULL,
        #                               PRIMARY KEY (`id`),
        #                               UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
        #                             """)
        if self.checkTableExists() is False:
            self.createAllBrandsTables()

        for car in self.car_dict.items():
            brand = self.extractDataFromURL(car[1])
            dbcursor.execute(f"""INSERT INTO {brand} (url, price) VALUES ('{car[1]}', {int(str(car[0]).replace(' ', ''))})""")

        dbcursor.close()
        self.db.commit()

    def checkTableExists(self):
        # dbcursor = self.db.cursor()
        # dbcursor.execute("""
        #     SELECT COUNT(*)
        #     FROM information_schema.tables
        #     WHERE table_name = '{0}'
        #     """.format(table_name.replace('\'', '\'\'')))
        # if dbcursor.fetchone()[0] == 1:
        #     dbcursor.close()
        #     return True
        #
        # dbcursor.close()
        # return False
        dbcursor = self.db.cursor()
        dbcursor.execute("""
                        SELECT COUNT(*)
                        FROM information_schema.tables
                        WHERE table_schema = 'otomotoprogram';
                        """)
        if dbcursor.fetchone()[0] > 140:
            dbcursor.close()
            return True
        dbcursor.close()
        return False

    def extractDataFromURL(self, url:str):
        temp_list = url.split('/')
        brand = temp_list[4].split('-')[0].lower() #table name
        return brand

    def createAllBrandsTables(self):
        with open('../Program files/brands.txt', 'r') as file:
            brands = [brand.strip().lower() for brand in file]
        dbcursor = self.db.cursor()
        dbcursor.execute("USE otomotoprogram;")
        for brand in brands:
            dbcursor.execute(
                f"""CREATE TABLE `otomotoprogram`.`{brand}` (
                                                  `id` INT NOT NULL AUTO_INCREMENT,
                                                  `url` LONGTEXT NOT NULL,
                                                  `price` INT NOT NULL,
                                                  PRIMARY KEY (`id`),
                                                  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
                                                """)
        dbcursor.close()
        self.db.commit()

# url = 'https://www.otomoto.pl/oferta/bmw-seria-5-piekne-rodzinne-bmw-520d-ID6Ei1VH.html'
# sql = SQL_Module(url)
# sql.create_table()