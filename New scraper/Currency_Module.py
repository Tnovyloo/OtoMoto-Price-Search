from forex_python.converter import CurrencyRates

class Currency:
    def __init__(self, car_dict, user_input):
        self.car_dict = car_dict
        self.user_input = user_input
        self.actual_currency = "PLN"

    def currency_rate(self):
        """Refactoring currency method"""
        c = CurrencyRates()
        self.user_input = input("Type currency (EUR, GBP, USD): ").upper()
        print("Please wait a second")
        currency = c.get_rate(self.actual_currency,
                              self.user_input)
        temp_dict = list(self.car_dict.items())
        self.car_dict.clear()
        self.actual_currency = self.user_input
        for key, value in temp_dict:
            if type(key) == str:
                new_key = round(float(key.replace(' ', '')) * currency)
            else:
                new_key = round(float(key) * currency)
            self.car_dict[new_key] = value

        print("\nChanging currency completed!")
        return self.actual_currency
