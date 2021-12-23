from abc import ABC
import scrapy
import requests
import os
from dotenv import load_dotenv
import html5lib
import bs4 as bs

class OtoMotoSpider(scrapy.Spider, ABC):
    name = "testspider"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        load_dotenv()
        self.url = os.environ.get('URL')
        self.response = requests.get(self.url).text
        self.soup = bs.BeautifulSoup(self.response, 'html5lib')
        self.page_list = [] #Holding all pages from 'Otomoto' website

    def start(self):
        self.find_page()

    def find_page(self):
        webpages = self.soup.findAll('span', class_="page")
        temp_list = []
        for page in webpages:
            temp_list.append(page.text)

        self.url = (self.url[:] + f"&page=0")
        for page in range(int(temp_list[-1]) + 1):
            self.page_list.append(self.url[:-1] + f"{page}")

        print(self.page_list)

    def start_requests(self):
        url = [self.page_list]
        for link in url:
            yield scrapy.Request(url=str(link), callback=self.parse)

    def parse(self, response, **kwargs):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        #Scrapy: get all data from pages. and scrap prices and links