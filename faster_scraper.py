import requests
import bs4 as bs
import threading

url = 'https://www.otomoto.pl/osobowe/bmw/seria-5/seg-sedan?search%5Bfilter_enum_generation%5D=gen-e39-1996-2003&search%5Border%5D=filter_float_price%3Adesc&search%5Bfilter_float_engine_capacity%3Afrom%5D=2490https://www.otomoto.pl/osobowe/bmw/seria-5/seg-sedan?search%5Bfilter_enum_generation%5D=gen-e39-1996-2003&search%5Border%5D=filter_float_price%3Adesc&search%5Bfilter_float_engine_capacity%3Afrom%5D=2490' # URL from user
response = requests.get(url).text # Response /// TODO check if i can remove that in constructor
soup = bs.BeautifulSoup(response, 'html.parser') # Creating BS object
price_cars_list = [] # List of prices of cars
link_cars_list = [] # List of URLs of cars
page_list = [] # List of pages from URL

def find_price():
    """Finding price of cars in page"""
    cars_price = soup.findAll('span',
                                   class_='ooa-epvm6 e1b25f6f8')  # Sometimes the class of 'span' on te web-page is changed
    for price in cars_price:
        price_cars_list.append(str(price.text).strip('PLN '))  # Appending price to list

def find_link():
    """Finding URL of car"""
    # cars_links = self.soup.findAll('div', class_='offer-item__title')
    cars_links = soup.findAll('h2',
                                   class_='e1b25f6f13 ooa-1mgjl0z-Text eu5v0x0')  # Sometimes the class of 'h2' on te web-page is changed

    for link in cars_links:
        link = link.find('a', href=True)
        link_cars_list.append(link['href'])  # Appending URL to list

def find_page():
    """Finding amount of pages"""
    # webpages = self.soup.findAll('span', class_="page")

    webpages = soup.findAll('a',
                                 class_='ooa-g4wbjr ekxs86z0')  # Sometimes the class of 'a' on te web-page is changed
    if len(webpages) == 0:  # Check if there is problem with finding amount of pages
        print("There is a problem with Otomoto servers")

    page_list = [page.text for page in webpages]  # Appending numbers of pages

    print(f'Amount of pages: {page_list[-1]}')
    return page_list

def go_to_page(url):
    pages = int(find_page()[-1])  # Last index from page_list is amount of pages
    func_url = (url[:] + f"&page=0")  # Append '$page=0' to URL with is used on next steps
    # for page in range(pages + 1):  # For range of pages
    #     response = requests.get(url).text  # Get the content from URL
    #     soup = bs.BeautifulSoup(response, 'html5lib')  # Scrap it with Beautifully Soup
    #     find_link()  # Use method to find URLs of cars
    #     find_price()  # Use method to find prices of cars
    #     func_url = (url[:-1] + f"{page}")  # Change last character from URL to next number
    #     print(f'Downloading data from page {page}')

    def start(url):
        response = requests.get(url).text
        soup = bs.BeautifulSoup(response, 'html5lib')
        find_link('tutaj przyjmyij jakis parametr') #TODO najpewniej przyjmij parametr z beatifull soup
        find_price('tutaj przyjmyij jakis parametr')

    return price_cars_list, link_cars_list

#TODO MULTITHREADING - moge przyjac url, ale musze przekazac w for loopie odpowiednie linki do zaczecia pobierania
# w kazdym threadzie, teraz jak to zrobic.