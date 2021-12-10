import bs4 as bs
import requests
import os
from dotenv import load_dotenv
import html5lib

load_dotenv()
url = os.environ.get('URL')
response = requests.get(url).text
soup = bs.BeautifulSoup(response, 'html5lib')

# print(response)

main = soup.findAll('main')
for element in main:
    element = element.find('article', 'optimus-app-5vxqem')
    print(element.text)
print(main)
