

# Builtin Imports
import os
import sys
import platform
import math 

from enum import Enum 

# Panda3D imports
from direct.showbase.ShowBase import ShowBase 

# from pandac.PandaModule import PandaSystem # Old version used for PandaSystem.getVersionString()
from panda3d.core import PandaSystem

# Royal Display Dictionary
RoyalDisplayData = {
    "Full Screen" : False,
    "Resolution HD+" :  (1600, 900), 
    "Resolution FHD" : (1920, 1080), 
    "Resolution QHD" : (2560, 1440), 
    "Resolution UHD" : (3840, 2160)
}


class RC_RoyalData: 
    """ Main Data used in RoyalData. These are not gameplay data. """

    # Class attributes
    RGameTitle = "Royal Palace"
    RWindowTitle = "Royal Palace Panda3D Micro-Game"
    RGameVersion = 1.0
    RPanda3dVersion = PandaSystem.getVersionString()
    RAuthor = "Yoann AMAR ASSOULINE"
    RCompany = "Goldanniyatech"

    RProjectTitle = RWindowTitle + " " + str(RGameVersion)

    def __new__(cls): 
        pass

    def __init__(self): 
        self.RWindowTitle = "Royal Palace Panda3D Micro-Game"

    @classmethod
    def get_RWindowTitle(cls):
        return cls.RWindowTitle

    @classmethod
    def get_ProjectTitle(cls): 
        return cls.RProjectTitle


class RC_RoyalProfileStats: 
    """ Profile Data for Players """


class RC_RoyalGameplayStats: 
    """ Gameplay Data """

    def __new__(cls): 
        pass 

    def __init__(self): 
        pass