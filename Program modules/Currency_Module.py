from forex_python.converter import CurrencyRates

class Currency:
    def __init__(self, car_dict, user_input):
        self.car_dict = car_dict # car dict with links and prize
        self.user_input = user_input # New currency
        self.actual_currency = "PLN" # Actual currency
        self.multiplier = 1 # Actual multiplier of currency

    def change_currency(self):
        """Refactoring currency method"""
        c = CurrencyRates() # Method with currency rates
        self.user_input = input("Type currency (EUR, GBP, USD): ").upper() # Input new currency
        print("Please wait a second")
        currency = c.get_rate(self.actual_currency,
                              self.user_input) # Get the rate of currency
        self.multiplier = currency # Set multiplier of currency
        temp_dict = list(self.car_dict.items()) # Converse car dict to list
        self.car_dict.clear() # Clear dict
        self.actual_currency = self.user_input # Change old currency to new
        for key, value in temp_dict:
            if isinstance(key, str):
            # if type(key) == str: # If key is string
                new_key = round(float(key.replace(' ', '')) * self.multiplier) # Change prize
            else: # Else key is not string
                new_key = round(float(key) * self.multiplier) # Change prize
            self.car_dict[new_key] = value # Save new key and old link

        print("\nChanging currency completed!")
        return self.actual_currency #Returning actual currency

    def currency_rate(self):
        return self.multiplier
