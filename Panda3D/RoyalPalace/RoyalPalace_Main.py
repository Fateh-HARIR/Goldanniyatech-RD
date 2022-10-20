#!/usr/bin/env python3

__author__ = "Yoann AMAR ASSOULINE" 

''' 
Royal Palace Main Module Doc

Project Coding Conventions: 
🎫 Variables start with "R"
🎫 Classes start with "Royal_" (except the main class, "RoyalPalace_" )
🎫 Collections start with "RC" 
🎫 Commands methods start with "RKey_" except the method defining keys (which should be "RCommands")

Versions support: 
Although some code is kept (& put as commentaries) for research purposes, only the following tools are supported: 
- Panda3D  

Packages 
- Panda3D (1.10.12)
- requests (2.28.1)

Export/ Import 3D Meshes 
- I export from Blender to gltf & convert it to BAM.

'''

# Builtin Imports
from genericpath import isfile
import os
import sys
import platform
import pathlib
import math 
import subprocess 

# Numpy import
import numpy

# Panda3D imports 
from direct.showbase.ShowBase import ShowBase 
from direct.actor import Actor 

# from pandac.PandaModule import PandaSystem # Old version used for PandaSystem.getVersionString()
from panda3d.core import PandaSystem

from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Vec4
from panda3d.core import WindowProperties 
from panda3d.core import Material

from direct.gui.DirectGui import * 

# RoyalPalace Imports ()
import Royal_DataManager 

# Royal Palace Debug Global Variables 
RDebugConfig = True
RDebugClearTerminal = True
RDebugWriteData = True
RDebugCleanFiles = True 

RDebugPanda3dContent = True # using asset from Panda3d SDK instead of my own asset (copy asset in ). ⚠️ Many features will NOT be available in this mode. 

# Royal Palace main data class
RoyalData = Royal_DataManager.Royal_Data

class RoyalPalace_Main(ShowBase): 
    """ Main class """

    def __new__(cls): 
        return object.__new__(cls)

    def __init__(self): 

        ShowBase.__init__(self)

        # Panda3d Window Properties 
        # ⚠️ Bug : display starts from 640*480, and isn't properly initialized in HD+

        RoyalWinProperties = WindowProperties() 
        RoyalWinProperties.setSize(Royal_DataManager.RCDisplayData["Resolution HD+"])
        RoyalWinProperties.setTitle (RoyalData.get_RProjectTitle())

        self.win.requestProperties(RoyalWinProperties) 

        # on-screen title 
        self.title = OnscreenText(text=RoyalData.get_RWindowTitle(), parent=self.a2dBottomCenter, fg=(1, 1, 1, 1), pos=(0, .1), )

        # Mouse Parameters
        self.disableMouse()
        
        # Background
        self.setBackgroundColor((0, 0, 0, 1))

        # Camera
        self.camera.setPos(0, 0, 0)
 
        # Calling DebugData class method (only if RDebugConfig variable is True)
        self.DebugData() 

        # Calling self class methods
        if RDebugPanda3dContent == True: 
            self.ModelLoader("panda-model.egg.pz")
        else: 
            self.LoadRoyalLevel()
        self.RCommands()

    def DebugData(self):
        """ Displaying Debug Data """

        # Writing Debug Data to Text file
        if RDebugWriteData == True: 
            DebugFile = open("RoyalPalace_DebugData.txt", "w")
            sys.stdout = DebugFile 

        # Clean terminal (checking Global Variable RDebugClearTerminal)
        if RDebugClearTerminal == True: 
            if os.name == 'nt': 
                os.system('cls')
            else: 
                'clear' 

        # System information
        print("SYSTEM INFO")
        print("OS: " + os.name)
        print("Python Version: " + platform.python_version())
        print("\n")

        print("AUTHOR INFO")
        print("Website: ", RoyalData.get_RWebsite())

        # Script information 
        print("Python Script: ", sys.argv[0])
        print("number of arguments: ", len(sys.argv))

        # Game version 
        print("ROYAL PALACE INFO")
        print("Panda 3d Version: " + RoyalData.get_RPanda3dVersion())

        print(RoyalData.get_RProjectTitle())
        print("\n")

        DebugFile.close()

        # Writing back to console
        if RDebugWriteData == True: 
            sys.stdout = sys.__stdout__

    def LoadRoyalLevel(self): 
        """ Loading every 3D model to display the menu """
        pass 

        # Environment 
        self.RoyalScene = self.loader.loadModel("test.bam")
        self.RoyalScene.reparentTo(self.render)
        self.RoyalScene.setScale(0.8, 0.8, 0.8) 
        self.RoyalScene.setPos(0, 0, 0)  

        # Temporary material 
        TestMaterial = Material()
        TestMaterial.setShininess(6.0)
        TestMaterial.setAmbient((0, 0, 1, 1))
        
        # Lights 

        RoyalAmbientLight = AmbientLight("ambient light") 
        RoyalAmbientLight.setColor(Vec4(0.5, 0.5, 0.5, 1))
        # Need to load the actual scene to attach the light. 
        # __builtins__['render'].setLight(self.RoyalAmbientLight) 
        
        # Characters 
        # 

        # Playable Character
        # 

    def ModelLoader(self, ModelPath, GScale=5): 
        """ Model loader to simplify how models are loaded in Python. 
            ModelLoader ()

            Parameters to add: static/ Skeletal; position; rotation; auto-animation (auto rotation, etc.)
        """
        
        self.CurrentModel = self.loader.loadModel("Panda3dModels/" + ModelPath)
        self.CurrentModel.reparentTo(self.render)

        # ⚠️ Bug :  Scale doesn't work yet
        self.CurrentModel.setScale(self.render, 0.1)

    def RCommands(self): 
        """ List of commands in the game (Keyboard only, at the moment) """
        
        # Escape to quit the game
        self.accept("escape", self.RKey_QuitRoyal)
        

    def RKey_QuitRoyal(self): 
        self.CleanUp() 
        sys.exit()

    def CleanUp(self): 
        print("Cleaning up Royal Palace Data")
        
        # Deleting Debug Text file
        if RDebugCleanFiles == True: 
            if os.path.isfile("RoyalPalace_DebugData.txt"): 
                os.remove("RoyalPalace_DebugData.txt")

# Launching the RoyalPalace Panda3D Application

if __name__ == "__main__": 
    RoyalPalaceApp = RoyalPalace_Main() 
    RoyalPalaceApp.run() 

else: 
    print("RoyalPalace is not __main__")