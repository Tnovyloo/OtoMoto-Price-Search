import bs4 as bs
import html5lib
import requests
import os
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        # self.URL = input("Provide Otomoto link with \nsearch criteria and price criteria: ")
        self.response = requests.get(self.URL).text
        # self.soup = bs.BeautifulSoup(self.response, 'html5lib')
        self.soup = bs.BeautifulSoup(self.response, 'html.parser')
        self.price_cars_list = []
        self.link_cars_list = []
        self.page_list = []
        self.index_list = []
        self.car_dict = {}
        self.user_input = 'PLN'

    def Start(self):
        self.DownloadPage()
        self.Work_with_data()

    def DownloadPage(self):

        def find_price():
            """Finding price of cars in page"""
            # cars_price = self.soup.findAll('span', class_='offer-price__number ds-price-number')
            cars_price = self.soup.findAll('span', class_='optimus-app-epvm6 e1b25f6f8')

            for price in cars_price:
                self.price_cars_list.append(str(price.text).strip('PLN '))

        def find_link():
            """Finding link of car"""
            # cars_links = self.soup.findAll('div', class_='offer-item__title')
            cars_links = self.soup.findAll('h2',
                                           class_='e1b25f6f13 optimus-app-1mgjl0z-Text eu5v0x0')

            for link in cars_links:
                # link = link.find('h2', class_='offer-title ds-title').text
                # link = link.find('a', class_='offer-title__link', href=True)
                link = link.find('a', href=True)
                self.link_cars_list.append(link['href'])

        def find_page(func):
            """Downloads amount of pages"""
            # webpages = self.soup.findAll('span', class_="page")
            webpages = self.soup.findAll('a', class_='optimus-app-g4wbjr ekxs86z0')
            # print(webpages)
            self.page_list = []
            for page in webpages:
                self.page_list.append(page.text)
            return func

        @find_page
        def go_to_page():
            """Going to all pages and downloads data to list"""
            # print(self.page_list)
            pages = int(self.page_list[-1]) + 1 #bład
            self.URL = (self.URL[:] + f"&page=0")
            for page in range(pages):
                self.response = requests.get(self.URL).text
                self.soup = bs.BeautifulSoup(self.response, 'html5lib')
                find_link()
                find_price()
                self.URL = (self.URL[:-1] + f"{page}")
                print(f'Wczytuję {self.URL}')

        go_to_page()

    def Work_with_data(self):

        def create_label():
            zip_iterator = zip(self.price_cars_list, self.link_cars_list)
            self.car_dict = dict(zip_iterator)

        def show_label():
            for prize, car in self.car_dict.items():
                print(f"Prize - {prize} {self.user_input} / Link - {car}")

        #TODO Wyswietlaj ceny w wybranej walucie
        def currency_rate():
            """Currency module"""
            c = CurrencyRates()
            self.user_input = input("Type currency (EUR, GBP, USD): ").upper()
            currency = c.get_rate('PLN', self.user_input)
            tempdict = list(self.car_dict.items())
            self.car_dict.clear()

            for key, value in tempdict:
                new_key = round(float(key.replace(' ', '')) * currency)
                self.car_dict[new_key] = value

            # for k, v in tempdict:
            #     new_k = round(float(k.replace(' ', '')) * currency)
            #     k = new_k
            #     print(f"{k}    {v}")

        create_label()
        show_label()
        currency_rate()
        show_label()

