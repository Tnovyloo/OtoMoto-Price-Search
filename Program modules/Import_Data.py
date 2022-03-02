import glob

class ImportData:
    def __init__(self):
        self.price_list = []
        self.link_list = []
        self.car_dict = {}
        self.currency = ''

    def import_from_txt(self):
        # print(glob.glob('./*.txt'))
        imports = glob.glob('./*.txt') # List of '.txt' files in dict
        if len(imports) > 0: # If imports is not empty
            for num, value in enumerate(imports, start=1):
                print(f"{num}. {value[2:]}") # Number is used to choose '.txt' file
            choice = int(input("Type a number of file: ")) # Input number
            if 1 <= choice <= len(imports): # If choice >= 1 and choice is smaller than length of imports
                name = imports[choice-1] # Chosen '.txt' file to open
                print(name[2:])
                with open(f"{name}", 'r') as file:
                    temp_list = []
                    for line in file:
                        # print(len(line.rstrip().split()))
                        temp_list.append(line.rstrip()) # Assign the appropriate data to variables
                        self.price_list.append(line.rstrip().split(" ")[1])
                        self.link_list.append(line.rstrip().split(" ")[5])
                        self.currency = line.rstrip().split(" ")[2]
        #TODO cos sie popsulo z wczytyaniem :)
    def return_currency(self):
        return self.currency