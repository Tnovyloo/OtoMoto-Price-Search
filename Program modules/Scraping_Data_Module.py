import requests
import bs4 as bs
from multiprocessing.dummy import Pool as ThreadPool
from URL_Module import check_type_of_url

class DownloadPage:
    def __init__(self, url):
        self.url = url # URL from user
        self.response = requests.get(self.url).text # Response /// TODO check if i can remove that in constructor
        self.soup = bs.BeautifulSoup(self.response, 'html.parser') # Creating BS object
        self.price_cars_list = [] # List of prices of cars
        self.link_cars_list = [] # List of URLs of cars
        self.page_list = [] # List of pages from URL

    def find_data(self, url):
        """Finding price of cars in page"""
        response = requests.get(url).text
        inner_soup = bs.BeautifulSoup(response, 'html5lib')
        cars_price = inner_soup.findAll('span',
                                        class_='ooa-epvm6 e1b25f6f8')  # Sometimes the class of 'span' on te web-page is changed
        for price in cars_price:
            self.price_cars_list.append(str(price.text).strip('PLN '))  # Appending price to list

        cars_links = inner_soup.findAll('h2',
                                        class_='e1b25f6f13 ooa-1mgjl0z-Text eu5v0x0')  # Sometimes the class of 'h2' on te web-page is changed
        for link in cars_links:
            link = link.find('a', href=True)
            self.link_cars_list.append(link['href'])  # Appending URL to list

    def find_page(self, site):
        """Finding amount of pages"""
        # webpages = self.soup.findAll('span', class_="page")
        response = requests.get(site).text
        soup = bs.BeautifulSoup(response, 'html5lib')

        webpages = soup.findAll('a',
                                class_='ooa-g4wbjr ekxs86z0')  # Sometimes the class of 'a' on te web-page is changed
        if len(webpages) == 0:  # Check if there is problem with finding amount of pages
            self.page_list = ['0']
        else:
            self.page_list = [page.text for page in webpages]  # Appending numbers of pages

        print(f'Amount of pages: {self.page_list[-1]}')
        return self.page_list

    def start(self):
        count_pages = int(self.find_page(self.url)[-1])  # Last index from page_list is amount of pages

        if check_type_of_url(self.url) is True:
            func_url = (self.url[:] + f"?page=0")  # Append '?page=0' to URL which is used on next steps
        else:
            func_url = (self.url[:] + f"&page=0")  # Append '$page=0' to URL which is used on next steps

        url_pages = [func_url[:-1] + f'{page}' for page in range(count_pages + 1)]

        pool = ThreadPool(4)
        results = pool.map(lambda x: self.find_data(x), url_pages)

        pool.close()
        pool.join()
        return self.price_cars_list, self.link_cars_list