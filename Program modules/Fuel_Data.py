import pandas as pd

URL = "https://www.autocentrum.pl/paliwa/ceny-paliw/"
table = pd.read_html(URL)
df = table[0]

def show_fuel_price():
    df_to_print = df['Unnamed: 0']
    print(df_to_print.to_string())

def find_price(province, multiplier, currency):
    # print(df[df['Unnamed: 0'].astype(str).str.contains(woj)])
    # print(df['Unnamed: 0'])
    user_province = df['Unnamed: 0'].iloc[int(province)]
    province_price = df[df['Unnamed: 0'].astype(str).str.contains(user_province)].values[0]

    if currency == 'PLN':
        multiplier = 1

    fuel_95 = round(((float(province_price[1:][0]) * 0.01) * multiplier), 2)
    fuel_98 = round(((float(province_price[1:][1]) * 0.01) * multiplier), 2)
    fuel_on = round(((float(province_price[1:][2]) * 0.01) * multiplier), 2)
    fuel_on_plus = round(((float(province_price[1:][3]) * 0.01) * multiplier), 2)
    fuel_lpg = round(((float(province_price[1:][4]) * 0.01) * multiplier), 2)

    print(f"Average price for fuels in '{province.capitalize()}' province\n"
          f"95 - {fuel_95} {currency}/l\n"
          f"98 - {fuel_98} {currency}/l\n"
          f"ON - {fuel_on} {currency}/l\n"
          f"ON+ - {fuel_on_plus} {currency}/l\n"
          f"LPG - {fuel_lpg} {currency}/l"
          )

# show_fuel_price()
# find_price(province= (input("Type province: ")), multiplier=1, currency='PLN')