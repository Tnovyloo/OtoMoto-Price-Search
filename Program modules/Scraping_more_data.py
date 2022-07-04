import requests
from bs4 import BeautifulSoup

class ScrapMoreData:
    def __init__(self, car_dict:dict):
        self.car_info = car_dict

    def find_more_data(self, url):
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')

        li_data = soup.findAll('li', class_='offer-params__item')
        # print(li_data)

        labels = []
        for label in li_data:
            label = label.find('span', class_='offer-params__label')
            labels.append(label.text)

        data = []
        for info in li_data:
            info = info.find('div', class_='offer-params__value')
            data.append(str(info.text).strip())

        # print(labels)
        # print(data)

        car_data = zip(labels, data)
        return car_data


    def get_more_data(self, data, url, price):
        result = {'URL': f'{url}',
                'cena': f'{price}',
                'Marka pojazdu' : '',
                'Model pojazdu' : '',
                'Rok produkcji' : '',
                'Wersja' : '',
                'Moc' : '',
                'Liczba drzwi' : '',
                'Rodzaj paliwa' : '',
                'Pojemność skokowa' : '',
                'Skrzynia biegów' : '',
                'Typ nadwozia' : '',
                'Kolor' : ''}

        for element, answer in list(data):
            if element in result:
                result[element] = answer

        return result

    def start(self, url, price):
        # for price, url in self.car_info.items():
        #     result_of_finding = self.find_more_data(url)
        #     result = self.get_more_data(result_of_finding, url, price)
        #     print(result)
        result_of_finding = self.find_more_data(url)
        result = self.get_more_data(result_of_finding, url, price)
        return result