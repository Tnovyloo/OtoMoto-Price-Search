class SavingToTxt:
    def __init__(self, car_dict, currency):
        #Constructing needed data types
        self.car_dict = car_dict
        self.currency = currency

    def saving_to_txt(self):
        """Saving in .txt method """
        name = input("Type file name: ") # Name of file
        print(f"\nSaving data to {name}.txt file\n")
        file = open(f"{name}.txt", 'a') # Create 'name' file
        if self.car_dict: # Check if dict is empty, empty dict returns False
            for key, value in self.car_dict.items(): # For each item, save it to txt
                file.writelines(f"Price {str(key).replace(' ', '')} {self.currency} - Link {value}\n")
            else:
                print('Your list is empty')
        file.close()
        print("\nSuccessfully completed!\n")