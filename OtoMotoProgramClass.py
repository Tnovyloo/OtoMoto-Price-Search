import bs4 as bs
import html5lib
import requests
import os
from dotenv import load_dotenv

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        self.response = requests.get(self.URL).text
        self.soup = bs.BeautifulSoup(self.response, 'html5lib')
        self.cars_list = []
        self.page_list = []

    def Start(self):
        print(self.URL)
        self.DownloadPage()
        self.Work_with_data()

    def DownloadPage(self):
        def find_price():
            """Finding price of cars in page"""
            cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')

            for price in cars_price:
                price = price.find_next('span')
                self.cars_list.append(price.text)

        def find_page(func):
            """Downloads amount of pages"""
            webpages = self.soup.findAll('span', class_="page")
            self.page_list = []
            for page in webpages:
                self.page_list.append(page.text)

            return func

        @find_page
        def go_to_page():
            """Going to all pages and downloads data to list"""
            for page in range(1, int(self.page_list[-1])):
                find_price()

        go_to_page()

    def Work_with_data(self):
        def sort_cars_list():
            """Sorting elements in cars list, removing 'od' and 'price'
            cause its advertising elements"""
            for element in self.cars_list:
                if element == "od":
                    index = self.cars_list.index("od")
                    del self.cars_list[index:index+2]
                else:
                    continue

        sort_cars_list()
        print(self.cars_list)