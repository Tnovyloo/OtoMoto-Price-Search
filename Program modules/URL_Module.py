import os

def get_url():
    with open('../User Files/url.txt', 'r+') as file: # Open url.txt with URLs
        txt_file_size = os.path.getsize('../User Files/url.txt')
        if txt_file_size > 0: # If storage of urls is not empty
            urls_list = [line.rstrip() for line in file] # Stores URls
            for num, element in enumerate(urls_list, start=1): # Simple user interface
                print(f"{num} - {element}")
            choice = input('Type number of URL or paste one: ')
            try: # If int(choice) returns ValueError then choice must be URL
                int(choice)
                url = urls_list[int(choice)-1]
                return url
            except ValueError:
                urls_list.append(choice)
                file.write(choice + '\n')
                return choice

        else: # Else if there is no URL in list
            print(f"There isn't urls in your saves yet, please paste one")
            temp = input('Type URL: ')
            # urls_list.append(temp)
            file.write(temp + '\n') # Write user Link
            # return urls_list[0]
            return temp


def save_url(url):
    """Simple function to save URL"""
    with open('../User Files/url.txt', 'a') as file:
        file.write(f'{url}\n')
        print('Your URL is now saved!')

def check_type_of_url(url):
    # print(url)
    temp_list = url.split('/')

    if indexExists(temp_list, 5) is False:
        # return print("True '?' - no url[5]") #TODO - Add this descriptions in Program logs
        return True
    else:
        if indexExists(temp_list, 6):
            # return print("False '&' - search in url[6]")
            return False
    if indexExists(temp_list, 5):
        if temp_list[5].__contains__("search"):
            # return print("False '&' - url[5] contains search")
            return False
        else:
            if indexExists(temp_list, 6):
                if temp_list[6].__contains__("search"):
                    # return print("False '&' - url[6] contains search")
                    return False
                else:
                    # return print("True '?' - url[6] no contains search")
                    return True
            # return print("True '?' - url no contains 'search'")
            return True

def indexExists(list, index):
    try:
        list[index]
        return True
    except IndexError:
        return False

#
# urls_to_tests = ["https://www.otomoto.pl/osobowe/bentley",  #true ?
#          "https://www.otomoto.pl/osobowe/alfa-romeo--bentley",  # true ?
#          "https://www.otomoto.pl/osobowe/alfa-romeo--bentley/seg-sedan",  # true ?
#          "https://www.otomoto.pl/osobowe/mercedes-benz/s-klasa",  # true ?
#          "https://www.otomoto.pl/osobowe/audi/a4/seg-cabrio?search%5Bfilter_enum_generation%5D=gen-b8-2007-2015",  # false &
#          "https://www.otomoto.pl/osobowe/mercedes-benz/s-klasa?search%5Bfilter_enum_generation%5D=gen-w140-1992-1998",  # false &
#          "https://www.otomoto.pl/osobowe/alfa-romeo--bentley/seg-sedan?search%5Bfilter_enum_fuel_type%5D=petrol&page=3", ] # false &

# loop = [example(text) for text in texts]