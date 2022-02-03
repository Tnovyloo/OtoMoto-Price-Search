import webbrowser

class BrowserModule:
    def __init__(self, link_cars):
        self.link_cars_list = link_cars

    def open_in_browser(self):
        """Opening links in browser"""
        x = 0 # Actual number of tabs
        count_of_tabs = abs(int(input("How much tabs you want to open?: "))) # Amount of opening tabs
        while True:
            user_input = input(f"Open {count_of_tabs} new tabs of auctions? (Y/N): ").lower() # Ask for user
            if user_input == "y": # If 'yes', go on next steps
                if count_of_tabs <= len(self.link_cars_list): # Check if count of tabs are smaller than list
                    for i in range(x, x+count_of_tabs):
                        if i > len(self.link_cars_list): # Check if 'i' are not greater than len of URLS
                            return False # End while loop
                        else:
                            webbrowser.open_new_tab(self.link_cars_list[i]) # Open new tab in default browser
                else:
                    print(f"{count_of_tabs} > {len(self.link_cars_list)}")
                    return False  # End while loop
                x += count_of_tabs # Iterate count of opened tabs
            else:
                return False # End while loop