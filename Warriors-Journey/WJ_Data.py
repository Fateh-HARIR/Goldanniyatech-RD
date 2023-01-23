
# Vanilla Python 3.11 

# To Do List 
# -> Implement a Save & a Menu (Start a new adventure ; Load adventure ; settings)

# Built-in Modules
import os 
import platform
import sys

# Variables
W_debug_mode = True 
W_debug_launch_app = False 

class WarriorsJourney_Data: 
    """ Warriors Journey Data Class
        Each property is using a @property decorator (with -> annotations). 
        Attributes here are useless and should be avoided unless they are temporarily need
    """

    # Basic Game Information
    game_author = "Yoann AMAR ASSOULINE"
    game_name = "Warriors Journey"
    game_version = 1.0

    player_name = None
    
    game_save_auto = False # Enabling auto-save feature

    # Characters Tuples
    main_characters = ("Warrior", "Fighter")
    Enemies = ()
    Monsters = ()
    Animals = ()

    def __init__(self): 

        if W_debug_mode is True: 
            # Cleaning Terminal
            if os.name == 'nt': 
                os.system ('cls')
            else: 
                os.system('clear')
            print("\n ✪ ✪  Warriors Journey DEBUG MODE ON  ✪ ✪ \n")

    # Game's name

    # Player's name

    @property
    def W_player_name (self) -> str: 
        """ The decorator makes it a property, and the arrow annotation explain what class is expected (string, in that case) """
        return self.player_name

    @W_player_name.setter
    def W_player_name(self, new_player_name) -> str: 
        if type(new_player_name) == str: 
            self.player_name = new_player_name
        if type(new_player_name) is not str: 
            print (f"⚠️ Error ⚠️ \n The player_name value is not a string but a {type(new_player_name)} instead! \n Please use the right data type!")

    @W_player_name.deleter
    def W_player_name(self) -> None: 
        self.player_name = None


class WarriorsJourney_Text: 
    """ Warriors Journey Text Class
        Specific class used to both stylize text and use fancy ASCII text. 
        
    """

    # Game items 
    game_title_stylized = """  
                        ██╗    ██╗ █████╗ ██████╗ ██████╗ ██╗ ██████╗ ██████╗ ███████╗         ██╗ ██████╗ ██╗   ██╗██████╗ ███╗   ██╗███████╗██╗   ██╗
                        ██║    ██║██╔══██╗██╔══██╗██╔══██╗██║██╔═══██╗██╔══██╗██╔════╝         ██║██╔═══██╗██║   ██║██╔══██╗████╗  ██║██╔════╝╚██╗ ██╔╝
                        ██║ █╗ ██║███████║██████╔╝██████╔╝██║██║   ██║██████╔╝███████╗         ██║██║   ██║██║   ██║██████╔╝██╔██╗ ██║█████╗   ╚████╔╝ 
                        ██║███╗██║██╔══██║██╔══██╗██╔══██╗██║██║   ██║██╔══██╗╚════██║    ██   ██║██║   ██║██║   ██║██╔══██╗██║╚██╗██║██╔══╝    ╚██╔╝  
                        ╚███╔███╔╝██║  ██║██║  ██║██║  ██║██║╚██████╔╝██║  ██║███████║    ╚█████╔╝╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║███████╗   ██║   
                         ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝     ╚════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝    
                        """

    # Menu items
    menu_main_menu = """ 
                    💥💥 Main Menu 💥💥
                     ╠1╣ New Adventure
                     ╠2╣ Load Adventure
                     ╠3╣ Options
                     """

    # Terminal Custom Elements (Font color, size, etc.)
    terminal_custom = { "Color-Red" : '\033[91m',
                        "Color-White" : '\033[0m', 
                        "Color-Blue" : '\033[94m'
                        }
    @property
    def W_game_title_stylized(self) -> str: 
        return self.game_title_stylized

    @property 
    def W_menu_main_menu(self) -> str: 
        return self.menu_main_menu

    # ⚠️ Not working for now
    @property 
    def W_terminal_custom(self, dict_value) -> dict.values: 
        return self.terminal_custom

if W_debug_launch_app is True: 

    # Testing WJ Data Class
    MyWJ_Data = WarriorsJourney_Data() 
    
    # Testing WJ Text Class
    MyWJ_Text = WarriorsJourney_Text()