import bs4 as bs
import html5lib
import requests
import os
from dotenv import load_dotenv

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        self.response = requests.get(self.URL)
        self.soup = bs.BeautifulSoup(self.response.content, 'html5lib')
        self.soupsecond = bs.BeautifulSoup(self.response.content, 'html.parser')
        self.cars_list = []

    def Start(self):
        print(self.URL)
        self.DownloadPage()
        # print(self.soupsecond.text)

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

        #Good way to find text in spans
        # cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')
        #
        # for price in cars_price:
        #     price = price.find_next('span')
        #     self.cars_list.append(price.text)
        #     # print(price.string)

        def Find_Span():
            cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')

            for price in cars_price:
                price = price.find_next('span')
                self.cars_list.append(price.text)

            webpageslist = []

            # webpages = self.soup.find_all("a", class_='optimus-app-g4wbjr ekxs86z0')
            # webpages = self.soup.find_all("ul", class_='pagination-list  optimus-app-1tibvxz')

            #TODO Get number from span to get count of pages
            webpages = self.soupsecond.find('div', class_='optimus-app-1oll9pn e19uumca7')
            print(webpages)
            print(webpageslist)
            # for page in webpages:
            #     # page = page.find_next('span')
            #     webpageslist.append(page)
            #     # print(page)
            #TODO Go to this pages and download data

            #TODO Sort Data in self.cars_list (There is a lot of mess data)
            # print(webpages)

        Find_Span()
        print(self.cars_list)
