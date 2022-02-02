def get_url():
    with open('url.txt', 'r+') as file:
        urls_list = []
        for line in file:
            urls_list.append(line.strip())

        if len(urls_list) > 0:
            for num, element in enumerate(urls_list, 1):
                print(f"{num} - {element}")
            choice = input('Type number of URL or type URL: ')
            try:
                int(choice)
                url = urls_list[int(choice)-1]
                return url
            except ValueError:
                urls_list.append(choice)
                file.write(choice)
                return choice
        else:
            print(f'There is no urls, please add one')
            temp = input('Type URL: ')
            urls_list.append(temp)
            file.write(temp)
            return urls_list[0]


def save_url(url):
    with open('url.txt', 'a') as file:
        file.write(f'{url}\n')
        # file.close()
        print('Your link was saved!')
