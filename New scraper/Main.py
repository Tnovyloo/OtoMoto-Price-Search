import os
from dotenv import load_dotenv
from Download_Page import DownloadPage
from Showing_Data import ShowingData
from Saving_Data import SavingToTxt
from Currency_Module import Currency
from Browser_Module import BrowserModule
from Import_Data import  ImportData
from URL_Module import get_url, save_url

class Start:
    def __init__(self):
        load_dotenv()
        # self.URL = os.environ.get("URL")
        self.user_input = 'PLN'
        self.URL = get_url()

        self.page = DownloadPage(url=self.URL)
        self.price_cars_list,\
        self.link_cars_list = self.page.downloading_page()

        self.show = ShowingData(cars_price=self.price_cars_list,
                           cars_link=self.link_cars_list,
                           user_input=self.user_input)

        self.car_dict = self.show.create_label()

        self.save = SavingToTxt(car_dict=self.car_dict,
                                currency=self.user_input)

        self.currency = Currency(car_dict=self.car_dict,
                            user_input=self.user_input)

        self.browser = BrowserModule(link_cars=self.link_cars_list)

        self.import_data = ImportData()

    def start(self):
        print('\nWelcome to OtoMoto Car-Scraper!\n')

        n = -1
        while n != 10:
            print('\nType:\n'
                  '1 - If you want to print label\n'
                  '2 - If you want to change Currency\n'
                  '3 - If you want to save auctions in .txt\n'
                  '4 - If you want to import auctions from .txt\n'
                  '5 - If you want to change URL\n'
                  '6 - If you want to save URL\n'
                  '7 - If you want to open auctions in Web-browser\n'
                  '8 - If you want to sort by ascending auctions\n'
                  '9 - If you want to sort by descending auctions\n'
                  '10 - If you want to close program\n')
            n = int(input("Type number: "))

            if n == 1:
                self.show.show_label()
                #TODO Price ascending
            if n == 2:
                self.user_input = self.currency.currency_rate()
                self.show.user_input = self.user_input
            if n == 3:
                #TODO jezeli lista jest pusta to powiadom o tym
                self.save.saving_to_txt()
            if n == 4:
                self.import_data.import_from_txt()
                self.show.user_input = self.import_data.userinput
                self.show.price_cars_list = self.import_data.price_list
            if n == 5:
                self.URL = input("Type URL from Otomoto: ")
                print("Now i will download data")
                self.page.downloading_page()
            if n == 6:
                save_url(self.URL)
            if n == 7:
                print()
                self.browser.open_in_browser()
            if n == 8:
                self.car_dict = self.show.price_asc()
            if n == 9:
                self.car_dict = self.show.price_dsc()
            if n == 10:
                break

start = Start()
start.start()