import pandas as pd

URL = "https://www.autocentrum.pl/paliwa/ceny-paliw/"
table = pd.read_html(URL)
df = table[0]

def show_fuel_price():
    print(df)

def find_price(province, multiplier, currency):
    # print(df[df['Unnamed: 0'].astype(str).str.contains(woj)])
    province_price = df[df['Unnamed: 0'].astype(str).str.contains(province)].values[0]

    fuel_95 = round(((float(province_price[1:][0]) * 0.01) * multiplier), 2)
    fuel_98 = round(((float(province_price[1:][1]) * 0.01) * multiplier), 2)
    fuel_on = round(((float(province_price[1:][2]) * 0.01) * multiplier), 2)
    fuel_on_plus = round(((float(province_price[1:][3]) * 0.01) * multiplier), 2)
    fuel_lpg = round(((float(province_price[1:][4]) * 0.01) * multiplier), 2)

    #TODO CHANGE CURRENCY
    print(f"Average price for fuels in '{province.capitalize()}' province\n"
          f"95 - {fuel_95} {currency}/l\n"
          f"98 - {fuel_98} {currency}/l\n"
          f"ON - {fuel_on} {currency}/l\n"
          f"ON+ - {fuel_on_plus} {currency}/l\n"
          f"LPG - {fuel_lpg} {currency}/l"
          )

# show_fuel_price()
# find_price(province= (input("Type province (for example 'małopolskie'): ").lower()))