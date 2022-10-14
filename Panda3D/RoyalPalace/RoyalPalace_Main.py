

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

from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Vec4
from pandac.PandaModules import WindowProperties 

from direct.gui.DirectGui import * 

# RoyalPalace Imports ()
import Royal_DataManager 


class RoyalPalaceMain(ShowBase): 
    """ Main class """

    def __new__(cls): 
        return object.__new__(cls)

    def __init__(self): 

        ShowBase.__init__(self)

        # Panda3d Window Properties 
        # ⚠️ Bug : display is changing in real-time and not initialized in HD+
        RoyalWinTitle = str(Royal_DataManager.RoyalData["Main Title"] + " Version " + Royal_DataManager.RoyalData["Game Version"])

        RoyalWinProperties = WindowProperties() 
        RoyalWinProperties.setSize(Royal_DataManager.RoyalDisplayData["Resolution HD+"])
        RoyalWinProperties.setTitle (RoyalWinTitle)

        self.win.requestProperties(RoyalWinProperties) 

        # on-screen title 
        self.title = OnscreenText(text=Royal_DataManager.RoyalData["Title"], parent=self.a2dBottomCenter, fg=(1, 1, 1, 1), pos=(0, .1), )

        # Mouse Parameters
        self.disableMouse()
        
        # Background
        self.setBackgroundColor((0, 0, 0, 1))

        # Camera
        self.camera.setPos(0, 0, 0)
 
        # Calling self class methods
        self.LoadModels()

    # ⚠️ I will transform this generic LoadModels into a method to directly load model, such as LoadModel(path, static/ skeletal, scale, etc.) with optional parameters. To Do only when models are imported from Blender.
    def LoadModels(self): 
        """ Loading every 3D model to display the menu """
        pass 

        # Environment 
        # self.RoyalScene = self.loader.loadModel("Path")
        # self.RoyalScene.reparentTo(self.render)
        # self.RoyalScene.setScale(1, 1, 1) 
        # self.RoyalScene.setPos(0, 0, 0)  

        # Lights 

        RoyalAmbientLight = AmbientLight("ambient light") 
        RoyalAmbientLight.setColor(Vec4(0.5, 0.5, 0.5, 1))
        # Need to load the actual scene to attach the light. 
        # __builtins__['render'].setLight(self.RoyalAmbientLight) 
        
        # Characters 
        # 

        # Playable Character
        # 
 
# Launching the RoyalPalace Panda3D Application

if __name__ == "__main__": 
    RoyalPalaceApp = RoyalPalaceMain() 
    RoyalPalaceApp.run() 
else: 
    print("RoyalPalaceMain is not __main__")
