class SavingToTxt:
    def __init__(self, car_dict, currency):
        self.car_dict = car_dict
        self.currency = currency

    def saving_to_txt(self):
        """Saving in .txt method """
        name = input("Type file name: ")
        print(f"\nSaving data to {name}.txt file\n")
        file = open(f"{name}.txt", 'a')

        for key, value in self.car_dict.items():
            file.writelines(f"Price {str(key).replace(' ', '')} {self.currency} - Link {value}\n")
        file.close()
        print("\nSuccessfully completed!\n")