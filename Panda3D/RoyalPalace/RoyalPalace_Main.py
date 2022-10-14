


from direct.showbase.ShowBase import ShowBase 

class RoyalPalaceMain(ShowBase): 

    def __init__(self): 

        ShowBase.__init__(self)

 
# Launching the RoyalPalace Panda3D Application

if __name__ == "__main__": 
    RoyalPalaceApp = RoyalPalaceMain() 
    RoyalPalaceApp.run() 
else: 
    print("This program will stop")

