class ShowingData:
    def __init__(self, cars_price, cars_link, user_input):
        self.user_input = user_input
        self.price_cars_list = cars_price
        self.link_cars_list = cars_link
        zip_iterator = zip(self.price_cars_list, self.link_cars_list)
        self.car_dict = dict(zip_iterator)

    def show_label(self):
        """Showing label"""
        for price, car in self.car_dict.items():
            print(f"Price - {price} {self.user_input} / Link - {car}")

    def create_label(self):
        """Returning dict"""
        return self.car_dict