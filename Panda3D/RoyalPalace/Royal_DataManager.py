

# Builtin Imports
import os
import sys
import platform
import math 

# Panda3D imports 
from direct.showbase.ShowBase import ShowBase 

# from pandac.PandaModule import PandaSystem # Old version used for PandaSystem.getVersionString()
from panda3d.core import PandaSystem

# RoyalPalace Main Dictionary
RoyalData = {
    "Title" : "Royal Palace Panda3D Micro-Game", 
    "Main Title" : "Royal Palace", 
    "Game Version" : "1.0",
    "Panda3D Version" : "test", # PandaSystem.getVersionString(), 
    "Author" : "Yoann AMAR ASSOULINE", 
    "Company" : "Goldanniyatech"
}

# Royal Display Dictionary
RoyalDisplayData = {
    "Full Screen" : False,
    "Resolution HD+" :  (1600, 900), 
    "Resolution FHD" : (1920, 1080), 
    "Resolution QHD" : (2560, 1440), 
    "Resolution UHD" : (3840, 2160)
}


class RoyalDataC (): 
    """ Main Data used in RoyalData. These are not gameplay data. """

    def __new__(cls): 
        pass

    def __init__(self): 
        pass

class RoyalProfileData (): 
    """ Profile Data for Players """

class RoyalGameplayData (): 
    """ Gameplay Data """

    def __new__(cls): 
        pass 

    def __init__(self): 
        pass