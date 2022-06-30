import requests
from bs4 import BeautifulSoup


urls = ["https://www.otomoto.pl/oferta/bmw-seria-5-m-pakiet-525i-192-km-bezowy-srodek-ID6EDngF.html",
        "https://www.otomoto.pl/oferta/bmw-seria-5-e39m-pakiet520imanualtopasblaupieknystan-ID6ED1By.html"]

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

result = list(find_more_data(urls[0]))
# print(result)

for element in result:
    print(element)


#TODO stworz nowa baze danych i tam dawaj szczegolowe info odnosnie aukcji, zrob
#odpowiedni schemat tabelii aby zawrzeć wymagane dane podane poniżej
# Requirements of data in auction:
# Marka pojazdu* - text
# Model pojazdu* - text
# Rok produkcji* - int
# Wersja* - text
# Moc* - int
# Liczba drzwi* - int
# Rodzaj paliwa* - text
# Pojemność skokowa* - int
# Skrzynia biegów* - text
# Typ nadwozia* - text
# Kolor* - text
