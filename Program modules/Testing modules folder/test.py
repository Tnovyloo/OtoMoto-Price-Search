import requests
from bs4 import BeautifulSoup

# urls = ["https://www.otomoto.pl/oferta/bmw-seria-5-mpakiet-imola-2-5i-170km-brc-skora-xenon-grzane-fotele-tempomat-pdc-ID6EIDBZ.html",
#         "https://www.otomoto.pl/oferta/audi-q3-ID6ELbSD.html",
#         "https://www.otomoto.pl/oferta/mercedes-benz-klasa-s-kamera-night-vision-zadbany-jasny-srodek-ID6E8pW0.html"]

def find_more_data(url):
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


def get_more_data(data):
    result = {'Marka pojazdu' : '',
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
#
# #Szybki przyklad
# # for element in urls: #zrob jakas tabele urls pobranych z scrap more data
# #     download_result = list(find_more_data(element))
# #     x = get_more_data(download_result)
# #     print(x) #włacz sql module
#
#

# #odpowiedni schemat tabelii aby zawrzeć wymagane dane podane poniżej, zautomatyzuj całe działanie w algorytmie do SQL dodatkowo zrób klase
# # Requirements of data in auction:
# # 'Marka pojazdu' text
# # 'Model pojazdu' text
# # 'Rok produkcji' int
# # 'Wersja' - text
# # 'Moc' int
# # 'Liczba drzwi' int
# # 'Rodzaj paliwa' text
# # 'Pojemność skokowa' int
# # 'Skrzynia biegów' text
# # 'Typ nadwozia' text
# # 'Kolor' text
#
