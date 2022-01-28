import glob

class ImportData:
    #potrzebujemy zwrocic self user input
    # price cars list
    # link cars list
    def __init__(self):
        self.price_list = []
        self.link_list = []
        self.car_dict = {}
        self.userinput = ''

    def import_from_txt(self):
        # print(glob.glob('./*.txt'))
        imports = glob.glob('./*.txt')
        if len(imports) > 0:
            for num, value in enumerate(imports, 1):
                print(f"{num}. {value[2:]}")
            choice = int(input("Type a number of file: "))
            if 1 <= choice <= len(imports):
                name = imports[choice-1]
                print(name[2:])
                with open(f"{name}", 'r') as file:
                    #odpowiednio przydziel wartosci do
                    # zmiennych ktore nastepnie zwroc
                    templist = []
                    for line in file:
                        templist.append(line.rstrip())
                        # print(len(line.rstrip().split()))
                        self.price_list.append(line.rstrip().split(" ")[1])
                        self.link_list.append(line.rstrip().split(" ")[5])
                        self.userinput = line.rstrip().split(" ")[2]

        # print(self.userinput)
        # print(self.price_list)
        # print(self.link_list)
