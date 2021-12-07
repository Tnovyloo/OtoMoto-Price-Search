import bs4 as bs
import requests
import os
from dotenv import load_dotenv
import lxml

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        self.response = requests.get(self.URL)
        self.soup = bs.BeautifulSoup(self.response.text, 'lxml')
        self.cars_list = []

    def Start(self):
        print(self.URL)
        # print(self.DownloadPage())
        self.DownloadPage()

    def DownloadPage(self):
        # cars_price = self.soup.find_all('span', class_='optimus-app-epvm6 e1b25f6f8')
        # cars_price = self.soup.find_all('span', attrs={'class':'optimus-app-epvm6 e1b25f6f8'})
        # cars_price = self.soup.find_all('span', class_='offer-price__number ds-price-number')
        cars_price = self.soup.find('span', class_='offer-price__number ds-price-number').contents[1]
        # <span class="offer-price__number ds-price-number">

        for price in cars_price:
            self.cars_list.append(price)
            print(price)

        # print(cars_price)


        # print(self.soup.find_all())
        #robimy petle w ktorej pobieramy pojedynczo article i sprwadzmy czy dla danego article parametry
        # sa wlasciwe, jezeli sa wlasciwe to dodajemy do cars_price (unikamy przede wszystkim innych ofert od naszych BMW

