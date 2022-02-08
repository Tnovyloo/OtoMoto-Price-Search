import pandas as pd

URL = "https://www.autocentrum.pl/paliwa/ceny-paliw/"
table = pd.read_html(URL)
df = table[0]

def show_fuel_price():
    print(df)

def find_price(province):
    # print(df[df['Unnamed: 0'].astype(str).str.contains(woj)])
    province_price = df[df['Unnamed: 0'].astype(str).str.contains(province)].values[0]

    #TODO change it to float
    fuel_95 = str(province_price[1:][0])
    fuel_98 = str(province_price[1:][1])
    fuel_on = str(province_price[1:][2])
    fuel_on_plus = str(province_price[1:][3])
    fuel_lpg = str(province_price[1:][4])

    #example
    print(round(float(fuel_95) * 10 ** -2, 2))
    print(round(float(fuel_95) * 0.01, 2))

    #TODO CHANGE CURRENCY
    print(f"Average price for fuels in '{province.capitalize()}' province\n"
          f"95 - {(fuel_95[0]) + '.' + (fuel_95[1:])} zł/l\n"
          f"98 - {(fuel_98[0]) + '.' + (fuel_98[1:])} zł/l\n"
          f"ON - {(fuel_on[0]) + '.' + (fuel_on[1:])} zł/l\n"
          f"ON+ - {(fuel_on_plus[0]) + '.' + (fuel_on_plus[1:])} zł/l\n"
          f"LPG - {(fuel_lpg[0]) + '.' + (fuel_lpg[1:])} zł/l"
          )

# show_fuel_price()
# find_price(province= (input("Type province (for example 'małopolskie'): ").lower()))