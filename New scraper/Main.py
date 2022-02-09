import os
from dotenv import load_dotenv
from Download_Page import DownloadPage
from Showing_Data import ShowingData
from Saving_Data import SavingToTxt
from Currency_Module import Currency
from Browser_Module import BrowserModule
from Import_Data import  ImportData
from URL_Module import get_url, save_url
from Fuel_Data import show_fuel_price ,find_price

class Start:
    def __init__(self):
        load_dotenv()
        # self.URL = os.environ.get("URL")
        self.actual_currency = 'PLN'
        self.currency_multiplier = 1
        self.URL = get_url()

        self.page_module = DownloadPage(url=self.URL)
        self.price_cars_list,\
        self.link_cars_list = self.page_module.downloading_page()

        self.show_data_module = ShowingData(cars_price=self.price_cars_list,
                                            cars_link=self.link_cars_list,
                                            user_input=self.actual_currency)

        self.car_dict = self.show_data_module.create_label()

        self.save_module = SavingToTxt(car_dict=self.car_dict,
                                       currency=self.actual_currency)

        self.currency_module = Currency(car_dict=self.car_dict,
                                        user_input=self.actual_currency)

        self.browser_module = BrowserModule(link_cars=self.link_cars_list)

        self.import_data_module = ImportData()


    def start(self):
        print('\nWelcome to OtoMoto Car-Scraper!\n')

        n = -1
        while n != 11:
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
                  '10 - If you want to print fuel prices\n'
                  '11 - If you want to close program\n')
            n = int(input("Type number: "))

            if n == 1: # Print label
                self.show_data_module.show_label()
            if n == 2: # Change currency
                self.actual_currency = self.currency_module.change_currency()
                self.show_data_module.user_input = self.actual_currency
                self.currency_multiplier = self.currency_module.currency_rate()
            if n == 3: # Save data to txt
                #TODO Module must save actual multipler to working fine
                self.save_module.saving_to_txt()
            if n == 4: # Import data from txt
                #TODO Module dont importing currency
                self.import_data_module.import_from_txt()
                self.show_data_module.user_input = self.import_data_module.userinput
                self.show_data_module.price_cars_list = self.import_data_module.price_list
            if n == 5: # Change URL
                self.URL = input("Type URL from Otomoto: ")
                print("Now i will download data")
                self.page_module.downloading_page()
            if n == 6: # Save URL
                save_url(self.URL)
            if n == 7: # Open in browser
                print()
                self.browser_module.open_in_browser()
            if n == 8: # Show by price ascending
                self.car_dict = self.show_data_module.price_asc()
            if n == 9: # Show by price descending
                self.car_dict = self.show_data_module.price_dsc()
            if n == 10: # Show fuel data
                show_fuel_price()
                find_price(province=(input("Type province (for example 'małopolskie'): ").lower()),
                           multiplier=self.currency_multiplier,
                           currency=self.actual_currency)
            if n == 11: # Break
                break
            #TODO Connect with MySQL and create database

start = Start()
start.start()