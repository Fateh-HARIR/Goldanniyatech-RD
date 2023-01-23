
import os 
import platform 
import sys
import time 

# Warriors Journey Modules
import WJ_Data

# Debug variables
BIOS_Tester = True

# WJ External Modules' classes instances
WJ_Data_BIOSInstance = WJ_Data.WarriorsJourney_Data()
WJ_Text_BIOSInstance = WJ_Data.WarriorsJourney_Text()

class WarriorsJourney_BIOS: 

    # BIOS Settings 
    DEBUG_TEXT = True
    QUICK_BOOT = False 
    QUICK_REBOOT = False # used when re-starting the game
    SAVE_DETECTOR = False

    def __init__ (self): 

        self.BIOS_TerminalCleaner()

        if self.DEBUG_TEXT is True: 
            print("𝓑𝓘𝓞𝓢 𝓘𝓷𝓲𝓽𝓲𝓪𝓵𝓲𝔃𝓪𝓽𝓲𝓸𝓷...")

            self.BIOS_properties()

    def BIOS_properties(self): 
        """ BIOS Properties Method
            Writing many properties & technical info
        """

        print("\n")

        # Automatically detect properties of this class (WarriorsJourney_BIOS)
        for a in dir(WarriorsJourney_BIOS): 
            if (a[:2] != "__"): 
                print("🟥 ", a, ":", getattr(WarriorsJourney_BIOS, a))

        print("\n")

        # Detecting some Hardware & Software information 
        HardwareSoftware_Info = {
            "Machine: " : platform.machine(), 
            "Architecture: " : platform.architecture(),
            "Processor: " : platform.processor(), 
            "System: " : platform.system(),
            "Python Version: " : platform.sys.version 
        }

        for key, value in HardwareSoftware_Info.items(): 
            print("🟦 ", key, value)

        print("\n")

    def BIOS_launch(self): 
        pass 

    def BIOS_screen(self): 
        pass

    def BIOS_TerminalCleaner(self): 
        
        if os.name == 'nt': 
            os.system ('cls')
        else: 
            os.system('clear')

    def startup_screen(self): 
        pass 

if BIOS_Tester is True: 

    MyWJ_BIOS = WarriorsJourney_BIOS()
