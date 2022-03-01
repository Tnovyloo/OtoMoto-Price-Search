import requests
import bs4 as bs
from multiprocessing.dummy import Pool as ThreadPool

url_main = 'https://www.otomoto.pl/osobowe/bmw/seria-5/seg-sedan?search%5Bfilter_enum_generation%5D=gen-e39-1996-2003&search%5Border%5D=filter_float_price%3Adesc&search%5Bfilter_float_engine_capacity%3Afrom%5D=2490https://www.otomoto.pl/osobowe/bmw/seria-5/seg-sedan?search%5Bfilter_enum_generation%5D=gen-e39-1996-2003&search%5Border%5D=filter_float_price%3Adesc&search%5Bfilter_float_engine_capacity%3Afrom%5D=2490' # URL from user
price_cars_list = [] # List of prices of cars
link_cars_list = [] # List of URLs of cars

def find_data(url):
    """Finding price of cars in page"""
    #zainicjowac tutaj nowa zmienna z klasa BS
    response = requests.get(url).text
    inner_soup = bs.BeautifulSoup(response, 'html5lib')
    cars_price = inner_soup.findAll('span',
                                   class_='ooa-epvm6 e1b25f6f8')  # Sometimes the class of 'span' on te web-page is changed
    for price in cars_price:
        price_cars_list.append(str(price.text).strip('PLN '))  # Appending price to list

    # price_cars_list = [str(price.text).strip('PLN ') for price in cars_price] #TODO test comprehension

    cars_links = inner_soup.findAll('h2',
                                   class_='e1b25f6f13 ooa-1mgjl0z-Text eu5v0x0')  # Sometimes the class of 'h2' on te web-page is changed

    for link in cars_links:
        link = link.find('a', href=True)
        link_cars_list.append(link['href'])  # Appending URL to list

def find_page(site):
    """Finding amount of pages"""
    # webpages = self.soup.findAll('span', class_="page")
    response = requests.get(site).text
    soup = bs.BeautifulSoup(response, 'html5lib')

    webpages = soup.findAll('a',
                                 class_='ooa-g4wbjr ekxs86z0')  # Sometimes the class of 'a' on te web-page is changed
    if len(webpages) == 0:  # Check if there is problem with finding amount of pages
        print("There is a problem with Otomoto servers")

    page_list = [page.text for page in webpages]  # Appending numbers of pages

    print(f'Amount of pages: {page_list[-1]}')
    return page_list

def start(site):
    count_pages = int(find_page(site)[-1])  # Last index from page_list is amount of pages
    func_url = (site[:] + f"&page=0")  # Append '$page=0' to URL with is used on next steps
    url_pages = [func_url[:-1] + f'{page}' for page in range(count_pages+1)]

    pool = ThreadPool(4)
    results = pool.map(lambda x: find_data(x), url_pages)

    pool.close()
    pool.join()
    # return price_cars_list, link_cars_list

start(url_main)

sample_dict = dict(zip(price_cars_list, link_cars_list))
for key, value in sample_dict.items():
    print(key, value)
