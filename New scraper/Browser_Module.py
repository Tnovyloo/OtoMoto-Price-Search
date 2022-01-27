import webbrowser

class BrowserModule:
    def __init__(self, link_cars):
        self.link_cars_list = link_cars

    def open_in_browser(self):
        """Opening in browser method"""
        x = 0
        count_of_tabs = abs(int(input("How much tabs you want to open?: "))) # Amount of opening tabs
        while True:
            user_input = input(f"Open {count_of_tabs} new tabs of auctions? (Y/N): ").lower()
            if user_input == "y":
                if count_of_tabs <= len(self.link_cars_list):
                    for i in range(x, x+count_of_tabs):
                        if i > len(self.link_cars_list):
                            return False
                        else:
                            webbrowser.open_new_tab(self.link_cars_list[i])
                else:
                    print(f"{count_of_tabs} > {len(self.link_cars_list)}")
                    return False

                x += count_of_tabs
            else:
                return False