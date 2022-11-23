#!/usr/bin/env python3


# Builtin Imports
import os
import sys
import platform
import math 
import requests

from enum import Enum 

# Panda3D imports
from direct.showbase.ShowBase import ShowBase 

# from pandac.PandaModule import PandaSystem # Old version used for PandaSystem.getVersionString()
from panda3d.core import PandaSystem

# Royal Display Dictionary
RCDisplayData = {
    "Full Screen" : False,
    "Resolution HD+" :  (1600, 900), 
    "Resolution FHD" : (1920, 1080), 
    "Resolution QHD" : (2560, 1440), 
    "Resolution UHD" : (3840, 2160)
}

class Royal_Data: 
    """ Main Data used in RoyalData. These are not gameplay data. """

    # Class attributes 
    R_GameTitle = "Royal Palace"
    R_WindowTitle = "Royal Palace Panda3D Micro-Game"
    R_GameVersion = 1.0
    R_Panda3dVersion = PandaSystem.getVersionString()
    R_Author = "Yoann AMAR ASSOULINE"
    R_Company = "Goldanniyatech"
    R_Website = "https://www.goldanniyatech.com/"

    RC_game_paused = False

    # Class attributes based on previous attributes
    R_ProjectTitle = R_WindowTitle + " " + str(R_GameVersion)

    # Class methods to retrieve attributes.
    def __new__(cls): 
        pass

    def __init__(self): 
        self.R_WindowTitle = "Royal Palace Panda3D Micro-Game"

    @classmethod
    def get_R_WindowTitle(cls):
        return cls.R_WindowTitle

    @classmethod
    def get_R_ProjectTitle(cls): 
        return cls.R_ProjectTitle

    @classmethod
    def get_R_Panda3dVersion(cls): 
        return cls.R_Panda3dVersion
    
    @classmethod 
    def get_R_Author(cls): 
        return cls.R_Author
    
    @classmethod
    def get_R_Company(cls): 
        return cls.R_Company

    @classmethod 
    def get_R_Website(cls):
        
        # Checking if Website is working with requests status_code (200 = it works)
        WebRequest = requests.get(cls.R_Website)
        if WebRequest.status_code == 200: 
            print(cls.R_Website)
        elif WebRequest.status_code == 404 : 
            print("Website unavailable")
        else:
            print("Website unavailable")
        return cls.R_Website

    @classmethod
    def get_RC_game_paused(cls): 
        return cls.RC_game_paused

    def set_RC_game_paused(cls, value): 
        if value == False: 
            cls.RC_game_paused = False 
        elif value == True:
            cls.RC_game_paused = True

class Royal_ProfileStats: 
    """ Profile Data for Players """

    def __new__(cls): 
        pass 

    def __init__(self): 
        pass

class RRoyal_GameplayStats: 
    """ Gameplay Data """

    def __new__(cls): 
        pass 

    def __init__(self): 
        pass