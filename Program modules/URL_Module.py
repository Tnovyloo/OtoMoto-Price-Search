def get_url():
    with open('url.txt', 'r+') as file: # Open url.txt with URLs
        urls_list = [] # Stores URls
        for line in file:
            urls_list.append(line.strip()) # Append striped line to list

        if len(urls_list) > 0: # If storage of urls is not empty
            for num, element in enumerate(urls_list, start=1): # Simple user interface
                print(f"{num} - {element}")
            choice = input('Type number of URL or type URL: ')
            try: # If int(choice) returns ValueError then choice must be URL
                int(choice)
                url = urls_list[int(choice)-1]
                return url
            except ValueError:
                urls_list.append(choice)
                file.write(choice)
                return choice
        else: # Else if there is no URL in list
            print(f'There is no urls, please add one')
            temp = input('Type URL: ')
            urls_list.append(temp)
            file.write(temp) # Write user Link
            return urls_list[0]


def save_url(url):
    """Simple function to save URL"""
    with open('url.txt', 'a') as file:
        file.write(f'{url}\n')
        print('Your link was saved!')
