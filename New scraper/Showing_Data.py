class ShowingData:
    def __init__(self, cars_price, cars_link, user_input):
        self.user_input = user_input # User chosen currency
        self.price_cars_list = cars_price # Prices list
        self.link_cars_list = cars_link # Links list
        zip_iterator = zip(self.price_cars_list, self.link_cars_list) # Create dict with prices and links
        self.car_dict = dict(zip_iterator)

    def create_label(self):
        """Returning created dict"""
        zip_iterator = zip(self.price_cars_list, self.link_cars_list) # Create dict from two lists
        self.car_dict = dict(zip_iterator) # Assign created dict
        return self.car_dict

    def show_label(self):
        """Showing 'Price', 'Currency', 'Link'"""
        for price, car in self.car_dict.items():
            print(f"Price - {price} {self.user_input} / Link - {car}")

    def price_asc(self):
        """Changes ordinary of prices by ascending"""
        #TODO STRIP PRICE / PROBLEM WITH PRICE PLN FIRST READ

        # sorted_dict = {str(k).strip(): self.car_dict[k] for k in sorted(self.car_dict)}
        temp_dict = list(self.car_dict.items()) # Temporary dict
        self.car_dict.clear() # Clear dict from all data

        for key, value in temp_dict:
            new_key = str(key).replace(' ', '') # Replace empty space in price
            # if type(key) == str:
            #     new_key = key.replace(' ', '')
            # else:
            #     new_key = str(key).replace(' ', '')
            self.car_dict[new_key] = value # Assign new key to value

        sorted_dict = {k: self.car_dict[k] for k in sorted(self.car_dict.keys())} #Sort dict
        self.car_dict = sorted_dict # Assign sorted dict to car dict

        return self.car_dict

    def price_dsc(self):
        """Changes ordinary of prices by descending"""
        temp_dict = list(self.car_dict.items())
        self.car_dict.clear()

        for key, value in temp_dict:
            new_key = str(key).replace(' ', '')  # Replace empty space in price
            # if type(key) == str:
            #     new_key = key.replace(' ', '')
            # else:
            #     new_key = str(key).replace(' ', '')
            self.car_dict[new_key] = value # Assign new key to value

        sorted_dict = {k: self.car_dict[k] for k in sorted(self.car_dict, reverse=True)}
        self.car_dict = sorted_dict # Assign sorted dict to car dict

        return self.car_dict