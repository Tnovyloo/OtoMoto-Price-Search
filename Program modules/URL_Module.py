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
