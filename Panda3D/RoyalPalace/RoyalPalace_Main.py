
# Builtin Imports
import os
import sys
import platform
import math 

# Panda3D imports 
from direct.showbase.ShowBase import ShowBase 
from direct.actor import Actor 

# from pandac.PandaModule import PandaSystem # Old version used for PandaSystem.getVersionString()
from panda3d.core import PandaSystem
from pandac.PandaModules import WindowProperties 

from direct.gui.DirectGui import * 

# RoyalPalace Imports 


# RoyalPalace Main Dictionary
RoyalData = {
    "Title" : "Royal Palace Panda3D Micro-Game", 
    "Main Title" : "Royal Palace", 
    "Game Version" : 1.0,
    "Panda3D Version" : PandaSystem.getVersionString(), 
    "Author" : "Yoann AMAR ASSOULINE", 
    "Company" : "Goldanniyatech"
}

class RoyalPalaceMain(ShowBase): 
    """ Main class """

    def __init__(self): 

        ShowBase.__init__(self)

        # Panda3d Window Properties 
        props = WindowProperties() 
        props.setTitle (RoyalData["Main Title"] + " Version " + str(RoyalData["Game Version"]))
        base.win.requestProperties(props) 

        # on-screen title 
        self.title = OnscreenText(text=RoyalData["Title"], parent=base.a2dBottomCenter, fg=(1, 1, 1, 1), pos=(0, .1), )

        # Background
        self.setBackgroundColor((0, 0, 0, 1))

        # Calling self class methods
        self.LoadModels()

    def LoadModels(self): 
        """ Loading every 3D model to display the menu """
        pass 

    
 
# Launching the RoyalPalace Panda3D Application

if __name__ == "__main__": 
    RoyalPalaceApp = RoyalPalaceMain() 
    RoyalPalaceApp.run() 
else: 
    print("RoyalPalaceMain is not __main__")

