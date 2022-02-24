import requests
import bs4 as bs

class DownloadPage:
    def __init__(self, url):
        self.url = url # URL from user
        self.response = requests.get(self.url).text # Response /// TODO check if i can remove that in constructor
        self.soup = bs.BeautifulSoup(self.response, 'html.parser') # Creating BS object
        self.price_cars_list = [] # List of prices of cars
        self.link_cars_list = [] # List of URLs of cars
        self.page_list = [] # List of pages from URL

    def downloading_page(self):
        def find_price():
            """Finding price of cars in page"""
            cars_price = self.soup.findAll('span', class_='ooa-epvm6 e1b25f6f8') # Sometimes the class of 'span' on te web-page is changed
            for price in cars_price:
                self.price_cars_list.append(str(price.text).strip('PLN ')) # Appending price to list

        def find_link():
            """Finding URL of car"""
            # cars_links = self.soup.findAll('div', class_='offer-item__title')
            cars_links = self.soup.findAll('h2',
                                           class_='e1b25f6f13 ooa-1mgjl0z-Text eu5v0x0') # Sometimes the class of 'h2' on te web-page is changed

            for link in cars_links:
                link = link.find('a', href=True)
                self.link_cars_list.append(link['href']) # Appending URL to list

        def find_page(func):
            """Finding amount of pages"""
            # webpages = self.soup.findAll('span', class_="page")
            webpages = self.soup.findAll('a', class_='ooa-g4wbjr ekxs86z0')  # Sometimes the class of 'a' on te web-page is changed
            if len(webpages) == 0: # Check if there is problem with finding amount of pages
                print("There is a problem with Otomoto servers")

            self.page_list = [page.text for page in webpages] # Appending numbers of pages

            print(f'Amount of pages: {self.page_list[-1]}')
            return func

        @find_page
        def go_to_page():
            """Going to all pages and downloads data to list"""
            pages = int(self.page_list[-1]) # Last index from page_list is amount of pages
            self.url = (self.url[:] + f"&page=0") # Append '$page=0' to URL with is used on next steps
            for page in range(pages+1): # For range of pages
                self.response = requests.get(self.url).text # Get the content from URL
                self.soup = bs.BeautifulSoup(self.response, 'html5lib') # Scrap it with Beautifully Soup
                find_link() # Use method to find URLs of cars
                find_price() # Use method to find prices of cars
                self.url = (self.url[:-1] + f"{page}") # Change last character from URL to next number
                print(f'Downloading data from page {page}')

        go_to_page()
        return self.price_cars_list, self.link_cars_list