
# Vanilla Python 3.11 

# To Do List 
# -> Implement a Save & a Menu (Start a new adventure ; Load adventure ; settings)

# Built-in Modules
import sys
import platform
import os
import time 

# Warriors Journey Modules
import WJ_BIOS
import WJ_Data

# Global variables 
enemies_list = []
bosses_dictionary= {}
vehicles_list = []

# Temporary variables
TEMP_save_detected = False 
quick_reboot_enabled = False
BIOS_key = False 

# Terminal Font Colors Dictionary 
terminal_colors = { "Red" : '\033[91m',
                    "White" : '\033[0m', 
                    "Blue" : '\033[94m'
                  }

# WJ External Modules' classes instances
WJ_BIOS_MainInstance = WJ_BIOS.WarriorsJourney_BIOS()
WJ_Data_MainInstance = WJ_Data.WarriorsJourney_Data()
WJ_Text_MainInstance = WJ_Data.WarriorsJourney_Text()

class WarriorsJourney_Main: 
    
    def __init__(self):

        # Initialization :: Cleaning Terminal
        if os.name == 'nt': 
            os.system ('cls')
        else: 
            os.system('clear')

        # Fake BIOS :: Boot Sequence
        if quick_reboot_enabled is False: 
            self.startup_screen()
        elif quick_reboot_enabled is True: 
            self.quick_reboot()

        # Checking if save is detected 
        if TEMP_save_detected is False:
            self.main_menu() 
        elif TEMP_save_detected is True: 
            pass

    def startup_screen(self): 
        """ Start-up Screen 
        
        """
        print(terminal_colors.get("Red") + WJ_Text_MainInstance.game_title_stylized + terminal_colors.get("White"))

        time.sleep(2)

    def fake_BIOS(self): 
        """ Fake BIOS 
            A simulated BIOS to tweak some console & display settings that have no impact on the game itself.
        """
        pass

    def quick_reboot(self): 
        """ Quick Reboot Method 
            Useful to reboot the game (& access the main menu) without having the startup screen again
        """
        self.main_menu()

    def main_menu(self): 
        # '\033[1m' is to get bold text 
        print(terminal_colors.get("Blue") + '\033[1m' + WJ_Text_MainInstance.W_menu_main_menu + terminal_colors.get("White"))

        main_menu_event = True 

        # Event loop for the main menu screen
        while main_menu_event is True:

            choice_player = input() 
            error_message = "🚨 WRONG CHOICE! TRY AGAIN! 🚨"

            if choice_player.isdigit() is False: 
                print(error_message)
            elif choice_player.isdigit() is True and int(choice_player) > 4: 
                print("👾 That number is way too high! 👾")
            else: 
                match int(choice_player): 
                    case 0: 
                        print("Are you kidding? Choice 0 doesn't exist!")
                    case 1: 
                        # Create random sentences and select one of them here (by calling a method, of course)
                        print("Awesome, warrior!")
                    case 2: 
                        print("Let's remember what happened...")
                    case 3: 
                        print("Something to change?")
                    case _: 
                        print("I don't understand what you just asked!")
                break


    def start_new_adventure(self): 

        # Printing first message
        print("💥 Warriors Journey: The Beginning 💥 \n \n")
        time.sleep(2)
        print("Hey... Who are you exactly?")

        WJ_Data_MainInstance.W_player_name = input() 
        WJ_Data_MainInstance.W_player_name = WJ_Data_MainInstance.W_player_name.capitalize() 

        # Printing & changing termikjnal colors. 
        print(terminal_colors.get("Red") + f'Welcome aboard, {WJ_Data_MainInstance.W_player_name}! \n Please take a seat... And enjoy this fantastic adventure!' + terminal_colors.get("White"))

        while_count = 5 
        while (while_count < 100): 
            while_count += 5
            print('⌛ Loading...', 'hey')
        
        print(type(WJ_Data_MainInstance.W_player_name))

    def load_adventure(self): 
        pass

    def game_over(self): 
        pass

    
# Launch the app

if __name__ == "__main__": 
    WarriorsJourney_App = WarriorsJourney_Main() 
else: 
    print("WarriorsJourney_Main is not __main__")