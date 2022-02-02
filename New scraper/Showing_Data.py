class ShowingData:
    def __init__(self, cars_price, cars_link, user_input):
        self.user_input = user_input
        self.price_cars_list = cars_price
        self.link_cars_list = cars_link
        zip_iterator = zip(self.price_cars_list, self.link_cars_list)
        self.car_dict = dict(zip_iterator)

    def create_label(self):
        """Returning dict"""
        zip_iterator = zip(self.price_cars_list, self.link_cars_list)
        self.car_dict = dict(zip_iterator)
        return self.car_dict

    def show_label(self):
        """Showing label"""
        for price, car in self.car_dict.items():
            print(f"Price - {price} {self.user_input} / Link - {car}")

    def price_asc(self):
        #TODO STRIP PRICE / PROBLEM WITH PRICE PLN FIRST READ

        # sorted_dict = {str(k).strip(): self.car_dict[k] for k in sorted(self.car_dict)}
        # sorted_dict = {k: self.car_dict[k] for k in sorted(self.car_dict)}
        # self.car_dict = sorted_dict
        # return self.car_dict

        temp_dict = list(self.car_dict.items())
        self.car_dict.clear()

        for key, value in temp_dict:
            if type(key) == str:
                new_key = key.replace(' ', '')
            else:
                new_key = str(key).replace(' ', '')
            self.car_dict[new_key] = value

        sorted_dict = {k: self.car_dict[k] for k in sorted(self.car_dict.keys())}
        self.car_dict = sorted_dict

        return self.car_dict

    def price_dsc(self):

        temp_dict = list(self.car_dict.items())
        self.car_dict.clear()

        for key, value in temp_dict:
            if type(key) == str:
                new_key = key.replace(' ', '')
            else:
                new_key = str(key).replace(' ', '')
            self.car_dict[new_key] = value

        sorted_dict = {k: self.car_dict[k] for k in sorted(self.car_dict, reverse=True)}
        self.car_dict = sorted_dict

        return self.car_dict