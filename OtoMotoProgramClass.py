import bs4 as bs
import requests
import os
from dotenv import load_dotenv

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        self.response = requests.get(self.URL)
        self.soup = bs.BeautifulSoup(self.response.text, "html.parser")
        self.cars_list = []

    def Start(self):
        print(self.URL)
        print(self.DownloadPage())
        self.DownloadPage()

    def DownloadPage(self):
        # cars_price = self.soup.find_all("span")
        cars_price = self.soup.find_all('span', class_="optimus-app-1nvnpye e1b25f6f5")

        for price in cars_price:
            self.cars_list.append(price)
            print(price)

        print(self.soup.find_all())
        #robimy petle w ktorej pobieramy pojedynczo article i sprwadzmy czy dla danego article parametry
        # sa wlasciwe, jezeli sa wlasciwe to dodajemy do cars_price (unikamy przede wszystkim innych ofert od naszych BMW

        # temp = self.soup.find_all("article", {'class': 'optimus-app-5vxqem e1b25f6f18'})
        # for article in temp:
        #     print(article)
