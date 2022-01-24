import bs4 as bs
import requests
import os
import webbrowser
from dotenv import load_dotenv
from forex_python.converter import CurrencyRates

class OtoMotoProgram:
    def __init__(self):
        load_dotenv()
        self.URL = os.environ.get("URL")
        # self.URL = input("Provide Otomoto link with \nsearch criteria and price criteria: ")
        self.response = requests.get(self.URL).text
        self.soup = bs.BeautifulSoup(self.response, 'html.parser')
        self.price_cars_list = []
        self.link_cars_list = []
        self.page_list = []
        self.index_list = []
        self.car_dict = {}
        self.user_input = 'PLN'

    def Start(self):
        print('\nWelcome to OtoMoto Car-Scraper!\n'
              'Now i will download data from your URL\n')

        self.DownloadPage()

        n = -1
        while n != 0:
            print('\nType:\n'
                  '1 - If you want to print label\n'
                  '2 - If you want to change Currency\n'
                  '3 - If you want to save auctions in .txt\n'
                  '4 - If you want to change URL\n'
                  '5 - If you want to open auctions in Web-browser\n'
                  '6 - If you want to close program\n')
            n = int(input("Type number: "))

            if n == 1:
                self.Showing_Data()
            if n == 2:
                self.Currency_method()
            if n == 3:
                self.Saving_To_Txt()
            if n == 4:
                self.URL = input("Type URL from Otomoto")
                print("Now i will download data")
                self.DownloadPage()
            if n == 5:
                print()
                self.Open_in_Browser()
            if n == 6:
                break

        # self.DownloadPage()
        # self.Work_with_data()

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
                link = link.find('a', href=True)
                self.link_cars_list.append(link['href'])

        def find_page(func):
            """Downloads amount of pages"""
            # webpages = self.soup.findAll('span', class_="page")
            webpages = self.soup.findAll('a', class_='optimus-app-g4wbjr ekxs86z0')
            self.page_list = []
            for page in webpages:
                self.page_list.append(page.text)
            return func

        @find_page
        def go_to_page():
            """Going to all pages and downloads data to list"""
            pages = int(self.page_list[-1]) + 2
            self.URL = (self.URL[:] + f"&page=0")
            for page in range(pages):
                self.response = requests.get(self.URL).text
                self.soup = bs.BeautifulSoup(self.response, 'html5lib')
                find_link()
                find_price()
                self.URL = (self.URL[:-1] + f"{page}")
                print(f'Downloading data from page {page}')

        go_to_page()

    def Showing_Data(self):
        """Printing labels"""
        def create_label():
            zip_iterator = zip(self.price_cars_list, self.link_cars_list)
            self.car_dict = dict(zip_iterator)

        def show_label():
            for price, car in self.car_dict.items():
                print(f"Price - {price} {self.user_input} / Link - {car}")

        #TODO price asc
        def price_asc():
            """Show price ascending"""
            temp_dict = list(self.car_dict.items())
            self.car_dict.clear()

            for key, value in temp_dict:
                new_key = key.replace(' ', '')
                self.car_dict[new_key] = value

            for key in sorted(self.car_dict.keys()):
                print(key)

        create_label()
        show_label()
        # price_asc()

    def Currency_method(self):
        """Refactoring currency method"""
        def currency_rate():
            """Currency module"""
            c = CurrencyRates()
            self.user_input = input("Type currency (EUR, GBP, USD): ").upper()
            currency = c.get_rate('PLN', self.user_input)
            temp_dict = list(self.car_dict.items())
            self.car_dict.clear()

            for key, value in temp_dict:
                new_key = round(float(key.replace(' ', '')) * currency)
                self.car_dict[new_key] = value

            print("Changing currency completed!")

        currency_rate()

    def Saving_To_Txt(self):
        zip_iterator = zip(self.price_cars_list, self.link_cars_list)
        self.car_dict = dict(zip_iterator)

        namefile = input("Type file name: ")
        print(f"\nSaving data to {namefile}.txt file\n")
        file = open(f"{namefile}.txt", 'a')
        for key, value in self.car_dict.items():
            file.writelines(f"Price {key} - Link {value}\n")
        file.close()
        print("\nSuccessfully completed!\n")

    def Open_in_Browser(self):
        """Opening in browser method"""
        x = 0
        count_of_tabs = int(input("How much tabs you want to open?: "))
        while True:
            user_input = input(f"Do you want to open {abs(count_of_tabs)} new tabs of auctions? (Y/N): ")
            if user_input.lower() == "y":
                if count_of_tabs <= len(self.link_cars_list):
                    for i in range(x, abs(x+count_of_tabs)):
                        webbrowser.open_new_tab(self.link_cars_list[i])
                else:
                    print(f"{count_of_tabs} > {len(self.link_cars_list)}")
                    return False

                x += count_of_tabs
            else:
                return False