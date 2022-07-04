from os import environ
import mysql.connector
from Scraping_more_data import ScrapMoreData

class SQL_MoreData:
    def __init__(self, car_dict:dict):
        self.car_dict = car_dict
        db_host = environ.get('DB_HOST')
        db_user = environ.get('DB_USER')
        db_password = environ.get('DB_PASSWORD')
        self.db = mysql.connector.connect(host=db_host,
                                          user=db_user,
                                          password=db_password,
                                          )
        self.scraper = ScrapMoreData(self.car_dict)

    def start(self):
        dbcursor = self.db.cursor()
        dbcursor.execute("CREATE DATABASE IF NOT EXISTS otomotoprogram_advanced;")
        dbcursor.execute("USE otomotoprogram_advanced;")

        if self.checkTableExists() is False:
            self.createAllBrandsTables()

        for car in self.car_dict.items():
            brand = self.extractDataFromURL(car[1])
            price = int(str(car[0]).replace(' ', ''))
            url = car[1]
            result = self.scraper.start(price=car[0], url=car[1])
            print(result)
            dbcursor.execute(f"""INSERT INTO {brand}
             (url, price, year, version, power,
             count_doors, fuel, capacity, transmission, body_type, color) 
            VALUES ('{url}',
                    {price},
                    {int(result.get("Rok produkcji"))},
                    '{result.get('Wersja')}',
                    {int(result.get('Moc').replace(" KM",""))},
                    {int(result.get('Liczba drzwi'))},
                    '{result.get('Rodzaj paliwa')}',
                    {int(result.get('Pojemność skokowa').replace(" cm3", "").replace(" ", ""))},
                    '{result.get('Skrzynia biegów')}',
                    '{result.get('Typ nadwozia')}',
                    '{result.get('Kolor')}'
            );""")


        dbcursor.close()
        self.db.commit()

    def checkTableExists(self):
        dbcursor = self.db.cursor()
        dbcursor.execute("""
                        SELECT COUNT(*)
                        FROM information_schema.tables
                        WHERE table_schema = 'otomotoprogram_advanced';
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
        dbcursor.execute("USE otomotoprogram_advanced;")
        for brand in brands:
            dbcursor.execute(
                f"""CREATE TABLE `otomotoprogram_advanced`.`{brand}` (
                                                  `id` INT NOT NULL AUTO_INCREMENT,
                                                  `url` LONGTEXT NOT NULL,
                                                  `price` INT NOT NULL,
                                                  `year` INT NOT NULL,
                                                  `version` LONGTEXT NOT NULL,
                                                  `power` INT NOT NULL,
                                                  `count_doors` INT NOT NULL,
                                                  `fuel` LONGTEXT NOT NULL,
                                                  `capacity` INT NOT NULL,
                                                  `transmission` LONGTEXT NOT NULL,
                                                  `body_type` LONGTEXT NOT NULL,
                                                  `color` LONGTEXT NOT NULL,
                                                  PRIMARY KEY (`id`),
                                                  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
                                                """)
        dbcursor.close()
        self.db.commit()

# # 'Marka pojazdu' text
# # 'Model pojazdu' text
# # 'Rok produkcji' int
# # 'Wersja' - text
# # 'Moc' int
# # 'Liczba drzwi' int
# # 'Rodzaj paliwa' text
# # 'Pojemność skokowa' int
# # 'Skrzynia biegów' text
# # 'Typ nadwozia' text
# # 'Kolor' text

# result = {'URL': f'{url}',
#                 'cena': f'{price}',
#                 'Marka pojazdu' : '',
#                 'Model pojazdu' : '',
#                 'Rok produkcji' : '',
#                 'Wersja' : '',
#                 'Moc' : '',
#                 'Liczba drzwi' : '',
#                 'Rodzaj paliwa' : '',
#                 'Pojemność skokowa' : '',
#                 'Skrzynia biegów' : '',
#                 'Typ nadwozia' : '',
#                 'Kolor' : ''}