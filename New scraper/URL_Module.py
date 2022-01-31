def get_url():
    with open('url.txt', 'r+') as file:

        urls_list = []
        for line in file:
            urls_list.append(line.strip())

        if len(urls_list) > 0:
            for num, element in enumerate(urls_list, 1):
                print(f"{num} - {element}")

        else:
            print(f'There is no urls, please add one')
            temp = input('Type URL: ')
            urls_list.append(temp)
            file.write(temp)
            print(f'{1} - {urls_list[0]}')

        choice = int(input('Type number of URL: '))
        url = urls_list[choice-1]
        file.close()
    return url

def save_url():
    #TODO
    pass