#!/usr/bin/env python3

''' Royal Palace Main Module Doc

Project Coding Conventions: 
🪙 Variables start with "R_"
🪙 Collection of Variables start with "RC_" 
🪙 Classes Methods start with "RM_"
🪙 Classes or Modules start with "Royal_" (except the main class, "RoyalPalace_" )
🪙 Commands methods start with "RKey_" except the method defining keys (which should be "RCommands_")

Versions support: 
Although some code is kept (& put as commentaries) for research purposes, only the following tools are supported: 
🪙 Panda3D (1.10.12)
🪙 requests (2.28.1)

Export/ Import 3D Meshes 
🪙 I export from Blender to gltf & convert it to BAM.

'''

from __future__ import annotations

# Module Dunders 
__author__ = "Yoann AMAR ASSOULINE" 
__version__ = "1.0.0"

# Python Standard Library (Builtin)
from genericpath import isfile
import os
import sys
import platform
import pathlib
import math 
import subprocess 

# Third-Party Python Library 
import numpy


# Panda3D imports 
from direct.showbase.ShowBase import ShowBase 
from direct.actor import Actor 
from direct.task import Task

# from pandac.PandaModule import PandaSystem # Old version used for PandaSystem.getVersionString()
from panda3d.core import PandaSystem

from panda3d.core import AmbientLight, DirectionalLight
from panda3d.core import Vec4
from panda3d.core import WindowProperties 
from panda3d.core import Material
from panda3d.core import LightLensNode
from panda3d.core import Fog
from panda3d.core import NodePath

from direct.gui.DirectGui import *

# RoyalPalace Imports ()
import Royal_DataManager
import Royal_ConfigVariables

# Royal Palace Debug Global Variables 
R_debug_config = True
R_debug_clear_terminal = True
R_debug_write_data = True
R_debug_clean_files = True 
R_debug_panda3d_camera = True

R_debug_panda3d_content = False # using asset from Panda3d SDK instead of my own asset (copy asset in ). ⚠️ Many features will NOT be available in this mode. 

# Royal Palace main data class
RoyalData = Royal_DataManager.Royal_Data

class RoyalPalace_Main(ShowBase): 
    """ Main Royal Palace class """

    def __new__(cls): 
        return object.__new__(cls)

    def __init__(self): 

        ShowBase.__init__(self)

        # Panda3d Window Properties 
        # ⚠️ Bug : display starts from 640*480, and isn't properly initialized in HD+

        Royal_win_properties = WindowProperties() 
        Royal_win_properties.setSize(Royal_DataManager.RCDisplayData["Resolution HD+"])
        Royal_win_properties.setTitle (RoyalData.get_R_ProjectTitle())

        self.win.requestProperties(Royal_win_properties) 

        # on-screen title 
        self.title = OnscreenText(text=RoyalData.get_R_WindowTitle(), parent=self.a2dBottomCenter, fg=(1, 1, 1, 1), pos=(0, .1), )
 
        # Mouse Parameters
        if R_debug_panda3d_camera is False: self.disableMouse()
        
        # Background
        self.setBackgroundColor((0, 0, 0, 1))

        # Camera
        self.camera.setPos(0, 0, 0)
 
        # Calling DebugData class method (only if R_debug_config variable is True)
        self.DebugData() 

        # Calling the Startup Screen R method & Loading the Commands method when the task itself has finished
        self.taskMgr.add(self.RM_StartUpTask, "RM_StartUp") 
 
        # Calling the Model Loader/ loading R method
        if R_debug_panda3d_content is True: 
            self.RM_ModelLoader("panda-model.egg.pz") 
        else: 
            self.RM_LoadLevels("RoyalPalace.bam")
        
    def DebugData(self):
        """ Displaying Debug Data """

        # Writing Debug Data to Text file
        if R_debug_write_data == True: 
            debug_file = open("RoyalPalace_DebugData.txt", "w")
            sys.stdout = debug_file 

        # Clean terminal (checking Global Variable R_debug_clear_terminal)
        if R_debug_clear_terminal == True: 
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
        print("Website: ", RoyalData.get_R_Website())

        # Script information 
        print("Python Script: ", sys.argv[0])
        print("number of arguments: ", len(sys.argv))

        # Game version 
        print("ROYAL PALACE INFO")
        print("Panda 3d Version: " + RoyalData.get_R_Panda3dVersion())

        print(RoyalData.get_R_ProjectTitle())
        print("\n")

        debug_file.close()

        # Writing back to console
        if R_debug_write_data == True: 
            sys.stdout = sys.__stdout__

    def RM_StartUpTask (self, task): 
        """ Using a StartUp Screen from the Panda3D logo """

        task_time = 3.0
        if R_debug_config is True: task_time = 1

        # Starting StartUp Task and showing Panda3D Game Engine logo
        if task.time == 0: 
            if R_debug_config is True: print("StartUp Task Starting")
            self.Panda3DScreen = OnscreenImage(image='Pics/StartUp_Panda3D.jpg', pos=(0, 0, 0), scale=(2, 1, 1))
        
        # Waiting 3 seconds before to remove the first image
        if task.time < task_time:
            return Task.cont
        
        self.Panda3DScreen.destroy()
        self.RCommands()
        return Task.done
        
    def RM_LoadLevels (self, current_level): 
        """ Loading every 3D model to display the menu """

        # Environment 
        self.RoyalScene = self.loader.loadModel("Royal_3D-Models/Levels/" + current_level)
        self.RoyalScene.reparentTo(self.render)
        self.RoyalScene.setScale(1, 1, 1) 
        self.RoyalScene.setPos(0, 0, 0)
        self.RoyalScene.setHpr(270, 0, 0)

        self.camera.setPos(100, 100, 0)

        # Updating RoyalPalace Materials
        #if (current_level == "RoyalPalace.bam"): 
        #    if R_debug_config is True: print(self.RoyalScene.findAllMaterials())

        #    CastleMat_Black = self.RoyalScene.findMaterial("CastleMat_Black")
        #    CastleMat_Black_Panda3DVersion = Material()
        #    CastleMat_Black_Panda3DVersion.setShininess(0)
        #    CastleMat_Black_Panda3DVersion.setAmbient((1, 0, 1,0))
        #    CastleMat_Black_Panda3DVersion.setDiffuse((1, 0, 1,0))
        #    self.RoyalScene.replaceMaterial(CastleMat_Black, CastleMat_Black_Panda3DVersion)

        ########################
        # Lights 
        ########################

        # Directional Light 
        self.RoyalDirLight = DirectionalLight("RL_DirectionalLight") 
        self.RoyalDirLight.setColor((1, 1, 1, 1))
        self.RoyalDirLight.setShadowCaster(True, 512, 512)
        self.RoyalDirLight_Node = self.render.attachNewNode(self.RoyalDirLight)
        self.RoyalDirLight_Node.setHpr(0, -40, 0)
        self.render.setLight(self.RoyalDirLight_Node) 

        # Ambient Light 
        self.RoyalAmbLight = AmbientLight("RL_AmbientLight")
        self.RoyalAmbLight.setColor((0.3, 0.3, 0.3, 1))
        self.RoyalAmbLight_Node = self.render.attachNewNode(self.RoyalAmbLight)
        self.render.setLight(self.RoyalAmbLight_Node)
        
        # Shadow Mapping
        self.render.setShaderAuto()

        ########################
        # Fog 
        ########################

        self.RoyalPalace_Fog = Fog("RC_Fog")
        self.RoyalPalace_Fog.setColor(0.8, 0, 0)
        self.RoyalPalace_Fog.setLinearRange(0, 1000)
        self.RoyalPalace_Fog.setLinearFallback(45, 160, 320)

        self.render.attachNewNode(self.RoyalPalace_Fog)
        self.render.setFog(self.RoyalPalace_Fog)

    def RM_ModelLoader(self, ModelName, GScale=5): 
        """ Model loader to simplify how models are loaded in Python. 
            RM_ModelLoader ()

            Parameters to add: static/ Skeletal; position; rotation; auto-animation (auto rotation, etc.)
        """
        
        self.CurrentModel = ""

        if R_debug_panda3d_content is True: 
            self.CurrentModel = self.loader.loadModel("Panda3dModels/" + ModelName)
        else: 
            self.CurrentModel = self.loader.loadModel(RoyalData.get_R_GamePath + ModelName)
            self.CurrentModel.reparentTo(self.render)

        # ⚠️ Bug :  Scale doesn't work yet
        self.CurrentModel.setScale(self.render, 0.1)

        # Characters 
        pass

        # Playable Characters
        pass

    def RCommands(self): 
        """ List of commands in the game (Keyboard only, at the moment) """
        
        # Escape to quit the game
        self.accept("escape", self.RKey_QuitRoyal)

        # Spacebar to display in-game menu
        self.accept("space", self.RKey_InGameMenuRoyal)
        

    def RKey_QuitRoyal(self): 
        if R_debug_config is True: print("RKey_QuitRoyal")
        self.CleanUp() 
        sys.exit()

    def RKey_InGameMenuRoyal(self):
        local_game_paused = RoyalData.get_RC_game_paused()
        

        if R_debug_config is True:
            print("RKey_InGameMenuRoyal")
            print("Spacebar pressed")
  
        if local_game_paused is False: 
            print ('R_paused_game True')
            #self.RoyalPalace_Esc_instructions = OnscreenText(text='Escape = Quit', parent=self.a2dLeftCenter, fg=(1, 1, 1, 1), pos=(0.3, 0.85))
            #self.RoyalPalace_Space_instructions = OnscreenText(text='Space = Menu', parent=self.a2dLeftCenter, fg=(1, 1, 1, 1), pos=(0.3, 0.75)) 

            # Instructions Loop
            instructions_dict = { "Esc": "Escape = Quit", 
                                  "Space": "Space = Menu"
                                }
            
            OnscreenText_pos_y = 0.9

            for instruction_key, instruction_value in instructions_dict.items(): 
                RoyalData.append_RC_OnScreenText_objects(OnscreenText(text=instruction_value, parent=self.a2dLeftCenter, fg=(1, 1, 1, 1), pos=(0.3, OnscreenText_pos_y)))
                OnscreenText_pos_y -= 0.1
            
            RoyalData.set_RC_game_paused(True)

        elif local_game_paused is True: 
            print ('R paused game false') 

            RoyalData.set_RC_game_paused(False)

            panda3d_text_objects = RoyalData.get_RC_OnScreenText_objects()
             
            for object in panda3d_text_objects: 
                object.destroy()

        else: 
            print("ERROR with R_paused_game Variable")

    def CleanUp(self): 
        print("Cleaning up Royal Palace Data")
        
        # Deleting Debug Text file
        if R_debug_clean_files == True: 
            if os.path.isfile("RoyalPalace_DebugData.txt"): 
                os.remove("RoyalPalace_DebugData.txt")

# Launching the RoyalPalace Panda3D Application

if __name__ == "__main__": 
    RoyalPalaceApp = RoyalPalace_Main() 
    RoyalPalaceApp.run() 

else: 
    print("RoyalPalace is not __main__")