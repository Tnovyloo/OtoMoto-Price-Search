# import os
from dotenv import load_dotenv
from Download_Page import DownloadPage
from Showing_Data import ShowingData
from Saving_Data import SavingToTxt
from Currency_Module import Currency
from Browser_Module import BrowserModule
from Import_Data import  ImportData
from URL_Module import get_url, save_url
from Fuel_Data import fuel_price_data, show_fuel_price

class Start:
    def __init__(self):
        load_dotenv()
        # self.URL = os.environ.get("URL")
        self.actual_currency = 'PLN' #
        self.currency_multiplier = 1 # PLN is the scraped currency
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

        n = -1
        while n != 11:
            # User interface
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
                self.show_data_module.currency = self.actual_currency
                self.currency_multiplier = self.currency_module.currency_rate()
                print(self.currency_multiplier)

            if n == 3: # Save data to txt
                self.save_module = SavingToTxt(car_dict=self.car_dict,
                                               currency=self.actual_currency)
                self.save_module.currency = self.actual_currency
                self.save_module.saving_to_txt()

            if n == 4: # Import data from txt
                self.import_data_module.import_from_txt() # Import from txt module
                self.show_data_module.currency = self.import_data_module.currency # Set value of currency in 'ShowingData' class
                self.show_data_module.price_cars_list = self.import_data_module.price_list # Set value of price list in 'ShowingData' class
                self.actual_currency = self.import_data_module.return_currency() # Return actual currency
                self.currency_module.actual_currency = self.actual_currency # Set actual currency to Currency class
                self.currency_multiplier = self.currency_module.currency_rate() # Get the currency rate

            if n == 5: # Change URL
                self.URL = input("Type URL from Otomoto: ")
                print("Now i will download data")
                # self.page_module.downloading_page()
                self.page_module.start()
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
                fuel_price_data(province=(input("Type number of province: ")),
                                multiplier=self.currency_multiplier,
                                currency=self.actual_currency)
            #TODO Connect with MySQL and create database
            # Create table that contains brand, model, generation, for example |BMW| |Series 5| |E39| |Price| |URL|
            # - Program could to recognize it automatically from URL or User have to input values.
            # - Create new brands tables when its new to our database.
            # - How its gonna work?
            #   - 0.Send all scraped data to Database module.
            #   - 1.From specific car URL find out what is it a car and model.
            #   - 2.Check if brand table exists.
            #           if not - Create table
            #                       Add data of model and price to Database
            #           if yes - Add data of model and price to Database
            #   - 3.Do it for each element in lists.

if __name__ == '__main__':
    start = Start()
    start.start()