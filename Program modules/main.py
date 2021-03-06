# import os
from dotenv import load_dotenv
from Scraping_Data_Module import DownloadPage
from Showing_Data_Module import ShowingData
from Saving_Data import SavingToTxt
from Currency_Module import Currency
from Browser_Module import BrowserModule
from Import_Data import  ImportData
from URL_Module import get_url, save_url
from Fuel_Data import fuel_price_data, show_fuel_price
from SQL_Module import SQL_Module
from SQL_more_data import SQL_MoreData

class Start:
    def __init__(self):
        load_dotenv()
        self.actual_currency = 'PLN' #
        self.currency_multiplier = 1 # PLN is the actual currency
        self.URL = get_url()

        self.page_module = DownloadPage(url=self.URL) # Creating Download page variable with current URL
        self.price_cars_list, self.urls_cars_list = self.page_module.start() # Run Download page module and assign scraped value from URL to variables

        self.show_data_module = ShowingData(cars_price=self.price_cars_list,
                                            cars_link=self.urls_cars_list,
                                            user_input=self.actual_currency) # Order data to User interface module

        self.car_dict = self.show_data_module.create_label() # Create dict - label with URLs to cars and their prices

        self.currency_module = Currency(car_dict=self.car_dict,
                                        user_input=self.actual_currency) # Create currency module class with actual currency and data

        self.browser_module = BrowserModule(link_cars=self.urls_cars_list) # Create browser module with URLs.

        self.import_data_module = ImportData() # Initialize Import data module

    def start(self):
        print('\nWelcome to OtoMoto Car-Scraper!\n')

        user_input = -1
        while user_input != 13:
            # User interface
            print('\nType:\n'
                  '1 - Print label\n'
                  '2 - Change Currency\n'
                  '3 - Save auctions in .txt\n'
                  '4 - Import auctions from .txt\n'
                  '5 - Change URL\n'
                  '6 - Save URL\n'
                  '7 - Open auctions in Web-browser\n'
                  '8 - Sort by ascending auctions\n'
                  '9 - Sort by descending auctions\n'
                  '10 - Print fuel prices\n'
                  '11 - Add data to MySQL database (a curtailed version)\n'
                  '12 - Add data to MySQL database (advanced version)\n'
                  '13 - Close program\n')
            user_input = int(input("Type number: "))

            if user_input == 1: # Print label
                self.show_data_module.show_label()

            if user_input == 2: # Change currency
                self.actual_currency = self.currency_module.change_currency()
                self.show_data_module.currency = self.actual_currency
                self.currency_multiplier = self.currency_module.currency_rate()
                print(self.currency_multiplier)

            if user_input == 3: # Save data to txt
                self.save_module = SavingToTxt(car_dict=self.car_dict,
                                               currency=self.actual_currency)
                self.save_module.currency = self.actual_currency
                self.save_module.saving_to_txt()

            if user_input == 4: # Import data from txt
                self.import_data_module.import_from_txt() # Import from txt module
                self.show_data_module.currency = self.import_data_module.currency # Set value of currency in 'ShowingData' class
                self.show_data_module.price_cars_list = self.import_data_module.price_list # Set value of price list in 'ShowingData' class
                self.actual_currency = self.import_data_module.return_currency() # Return actual currency
                self.currency_module.actual_currency = self.actual_currency # Set actual currency to Currency class
                self.currency_multiplier = self.currency_module.currency_rate() # Get the currency rate

            if user_input == 5: # Change URL
                # self.URL = input("Type URL from Otomoto: ")
                # print("Now i will download data")
                # # self.page_module.downloading_page()
                # self.page_module.start()
                Start()

            if user_input == 6: # Save URL
                save_url(self.URL)

            if user_input == 7: # Open in browser
                print()
                self.browser_module.open_in_browser()

            if user_input == 8: # Show by price ascending
                self.car_dict = self.show_data_module.price_asc()

            if user_input == 9: # Show by price descending
                self.car_dict = self.show_data_module.price_dsc()

            if user_input == 10: # Show fuel data
                show_fuel_price()
                fuel_price_data(province=(input("Type number of province: ")),
                                multiplier=self.currency_multiplier,
                                currency=self.actual_currency)

            if user_input == 11: #Use SQL module
                db = SQL_Module(self.URL, self.car_dict, self.actual_currency)
                db.start()

            if user_input == 12: #Use advanced SQL module
                db = SQL_MoreData(self.car_dict)
                db.start()


if __name__ == '__main__':
    start = Start()
    start.start()