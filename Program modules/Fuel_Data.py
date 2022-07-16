import pandas as pd

URL = "https://www.autocentrum.pl/paliwa/ceny-paliw/"
table = pd.read_html(URL)
df = table[0]
df.rename(columns={'Unnamed: 0':'Provinces'}, inplace=True)

def show_fuel_price():
    # print("Dataframe columns:", df.columns)
    df_to_print = df['Provinces']
    print(df_to_print.to_string())

def fuel_price_data(province, multiplier, currency):
    """Getting price from specific province
    province -> its number from 0-16 meaning as province
    multiplier -> its multiplier from PLN to current currency
    currency -> its actual currency to print in program"""
    user_province = df['Provinces'].iloc[int(province)]
    province_price = df[df['Provinces'].astype(str).str.contains(user_province)].values[0]

    if currency == 'PLN':
        multiplier = 1

    # fuel_95 = round(((float(province_price[1:][0]) * 0.01) * multiplier), 2)
    # fuel_98 = round(((float(province_price[1:][1]) * 0.01) * multiplier), 2)
    # fuel_on = round(((float(province_price[1:][2]) * 0.01) * multiplier), 2)
    # fuel_on_plus = round(((float(province_price[1:][3]) * 0.01) * multiplier), 2)
    # fuel_lpg = round(((float(province_price[1:][4]) * 0.01) * multiplier), 2)


    # print(f"Average price for fuels in '{province.capitalize()}' province\n"
    #       f"95 - {fuel_95} {currency}/l\n"
    #       f"98 - {fuel_98} {currency}/l\n"
    #       f"ON - {fuel_on} {currency}/l\n"
    #       f"ON+ - {fuel_on_plus} {currency}/l\n"
    #       f"LPG - {fuel_lpg} {currency}/l"
    #       )

    fuels = [round(((float(province_price[1:][i]) * 0.01) * multiplier), 2) for i in range(5)]
    # print(fuels)

    print(f"Average price for fuels in '{user_province.capitalize()}' province\n"
          f"95 - {fuels[0]} {currency}/l\n"
          f"98 - {fuels[1]} {currency}/l\n"
          f"ON - {fuels[2]} {currency}/l\n"
          f"ON+ - {fuels[3]} {currency}/l\n"
          f"LPG - {fuels[4]} {currency}/l"
          )

# if __name__ == "__main__":
#    # stuff only to run when not called via 'import' here
#    show_fuel_price()
#    fuel_price_data()

