import bs4 as bs
import html5lib
import requests
import os
import re
from dotenv import load_dotenv

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        self.response = requests.get(self.URL)
        # self.soup = bs.BeautifulSoup(self.response.text, 'html.parser')
        self.soup = bs.BeautifulSoup(self.response.content, 'html5lib')

        self.cars_list = []

    def Start(self):
        print(self.URL)
        self.DownloadPage()

    def DownloadPage(self):
        # cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')


        # cars_price = self.soup.find('span', class_='offer-price__number ds-price-number').contents[1]
        # for price in cars_price:
        #     self.cars_list.append(price)
        #     print(price)
        #
        # print(self.cars_list)

        # cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')
        # for price in cars_price:
        #     self.cars_list.append(price.contents[1])
        #     print(price)
        #
        # print(len(cars_price) ,"\n", cars_price[0])

        cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')

        for price in cars_price:
            price = price.find_next('span')
            self.cars_list.append(price.text)
            # print(price.string)

        # print(len(cars_price))
        print(self.cars_list)


