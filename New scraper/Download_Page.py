import requests
import bs4 as bs

class DownloadPage:
    def __init__(self, url):
        self.url = url
        self.response = requests.get(self.url).text
        self.soup = bs.BeautifulSoup(self.response, 'html.parser')
        self.price_cars_list = []
        self.link_cars_list = []
        self.page_list = []

    def downloading_page(self):
        def find_price():
            """Finding price of cars in page"""
            # cars_price = self.soup.findAll('span', class_='offer-price__number ds-price-number')
            # cars_price = self.soup.findAll('span', class_='optimus-app-epvm6 e1b25f6f8')
            cars_price = self.soup.findAll('span', class_='ooa-epvm6 e1b25f6f8')
            for price in cars_price:
                self.price_cars_list.append(str(price.text).strip('PLN '))

        def find_link():
            """Finding link of car"""
            # cars_links = self.soup.findAll('div', class_='offer-item__title')
            cars_links = self.soup.findAll('h2',
                                           class_='e1b25f6f13 ooa-1mgjl0z-Text eu5v0x0')

            for link in cars_links:
                link = link.find('a', href=True)
                self.link_cars_list.append(link['href'])

        def find_page(func):
            """Downloads amount of pages"""
            # webpages = self.soup.findAll('span', class_="page")
            # webpages = self.soup.findAll('a', class_='optimus-app-g4wbjr ekxs86z0')
            webpages = self.soup.findAll('a', class_='ooa-g4wbjr ekxs86z0')
            # TODO Small issue with otomoto
            if len(webpages) == 0:
                print("There is a problem with Otomoto servers")

            self.page_list = []
            for page in webpages:
                self.page_list.append(page.text)
            print(self.page_list)
            return func

        @find_page
        def go_to_page():
            """Going to all pages and downloads data to list"""
            pages = int(self.page_list[-1]) + 1
            self.url = (self.url[:] + f"&page=0")
            for page in range(pages):
                self.response = requests.get(self.url).text
                self.soup = bs.BeautifulSoup(self.response, 'html5lib')
                find_link()
                find_price()
                self.url = (self.url[:-1] + f"{page}")
                print(f'Downloading data from page {page}')

        go_to_page()
        return self.price_cars_list, self.link_cars_list