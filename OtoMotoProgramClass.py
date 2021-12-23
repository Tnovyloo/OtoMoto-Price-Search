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
        self.price_cars_list = []
        self.link_cars_list = []
        self.page_list = []
        self.index_list = []

    def Start(self):
        print(self.URL)
        self.DownloadPage()
        # self.Work_with_data()

    def DownloadPage(self):

        def find_price():
            """Finding price of cars in page"""
            cars_price = self.soup.findAll('span', class_='offer-price__number ds-price-number')
            for price in cars_price:
                # price = price.find_next('span')
                price = price.find('span')
                self.price_cars_list.append(price.text)

        def find_link():
            cars_links = self.soup.findAll('div', class_='offer-item__title')
            index = 0
            for link in cars_links:
                # link = link.find('h2', class_='offer-title ds-title').text
                link = link.find('a', class_='offer-title__link', href=True)
                self.link_cars_list.append(link['href'])
                # key = 'otomotoklik.pl'
                # if key not in link['href']:
                #     self.link_cars_list.append(link['href'])
                #     index += 1
                # else:
                #     self.index_list.append(index)
                #     index += 1
                #     continue

        def find_page(func):
            """Downloads amount of pages"""
            webpages = self.soup.findAll('span', class_="page")
            print(webpages)
            self.page_list = []
            for page in webpages:
                self.page_list.append(page.text)
            return func

        @find_page
        def go_to_page():
            """Going to all pages and downloads data to list"""
            print(self.page_list)
            pages = int(self.page_list[-1]) + 1
            self.URL = (self.URL[:] + f"&page=0")
            for page in range(pages):
                self.response = requests.get(self.URL).text
                self.soup = bs.BeautifulSoup(self.response, 'html5lib')
                find_link()
                find_price()
                self.URL = (self.URL[:-1] + f"{page}")
                print(self.URL)


        go_to_page()
        # print(f'indexes of otomotoklik is: {self.index_list}')
        # print(self.response)
    def Work_with_data(self):

        def sort_cars_list():
            """Sorting elements in cars list, removing 'od' and 'price'
            cause its advertising elements"""
            # for element in self.price_cars_list:
            #     if element == "od":
            #         index = self.price_cars_list.index("od")
            #         del self.price_cars_list[index:index + 2]
            #
            #     else:
            #         continue
            for element in self.price_cars_list:
                if element == "od":
                    index = self.price_cars_list.index("od")
                    # del self.price_cars_list[index: index + 1]
                    del self.price_cars_list[index]

                else:
                    continue

        def sort_price_list():
            for element in self.index_list:
                self.price_cars_list.pop(element)

        def show_label():
            zip_iterator = zip(self.price_cars_list, self.link_cars_list)
            car_dict = dict(zip_iterator)
            for prize, car in car_dict.items():
                print(f"Prize - {prize} PLN/ Link - {car}")

        sort_cars_list()
        # sort_price_list()
        show_label()

        #TODO Napraw wyszukiwanie ceny i hrefu, zrob to w jednej funkcji aby sie to nie rozjezdżało
        #TODO Sprobowac zrobic powyzszy punkt w Selenium

        #TODO Sortuj wyniki rosnaco, malejaco, wybierz dany przedział ceny
        #TODO Wyswietlaj ceny w wybranej walucie


        # print(self.price_cars_list)
        # print(self.link_cars_list)
        # print(len(self.link_cars_list), len(self.price_cars_list))
        # # print(self.link_cars_list)
        # print()