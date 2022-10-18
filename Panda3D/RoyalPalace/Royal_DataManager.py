#!/usr/bin/env python3


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
    RGameTitle = "Royal Palace"
    RWindowTitle = "Royal Palace Panda3D Micro-Game"
    RGameVersion = 1.0
    RPanda3dVersion = PandaSystem.getVersionString()
    RAuthor = "Yoann AMAR ASSOULINE"
    RCompany = "Goldanniyatech"
    RWebsite = "https://www.goldanniyatech.com/"

    # Class attributes based on previous attributes
    RProjectTitle = RWindowTitle + " " + str(RGameVersion)

    # Class methods to retrieve attributes.
    def __new__(cls): 
        pass

    def __init__(self): 
        self.RWindowTitle = "Royal Palace Panda3D Micro-Game"

    @classmethod
    def get_RWindowTitle(cls):
        return cls.RWindowTitle

    @classmethod
    def get_RProjectTitle(cls): 
        return cls.RProjectTitle

    @classmethod
    def get_RPanda3dVersion(cls): 
        return cls.RPanda3dVersion
    
    @classmethod 
    def get_RAuthor(cls): 
        return cls.RAuthor
    
    @classmethod
    def get_RCompany(cls): 
        return cls.RCompany

    @classmethod 
    def get_RWebsite(cls): 
        return cls.RWebsite


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