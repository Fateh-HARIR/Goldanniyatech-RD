#!/usr/bin/env python3

# To Do List 
# transform @classmethods into @properties 

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

class Royal_Data_Class: 
    """ Main Data used in RoyalData. These are not gameplay data. """

    # Game Class attributes 
    game_path = "" 
    game_title = "Royal Palace"
    game_version = 1.0
    game_author = "Yoann AMAR ASSOULINE"
    game_company = "Goldanniyatech"
    game_website = "https://www.goldanniyatech.com/"
    window_title = str("Royal Palace Panda3D Micro-Game")
    panda3d_version = PandaSystem.getVersionString()

    # In-Game Class Attributes
    ingame_collectible_coins = 0

    # Menu Class Attributes
    menu_pause = False
    menu_OnScreenText_objects = []
    menu_settings_fog = False

    # Class Attributes based on previous attributes
    game_project_title = window_title + " " + str(game_version)

    ########################
    # Meta-Game Attributes (Read-only)
    ########################

    def __new__(cls): 
        pass

    def __init__(self): 
        pass

    @property 
    def R_GamePath(self) -> str: 
        return self.game_path

    @property
    def R_window_title(self) -> str:
        return self.window_title

    @R_window_title.setter
    def R_window_title(self, new_window_title) -> str:
        self.window_title = new_window_title
        return self.window_title

    @property
    def R_ProjectTitle(self) -> str: 
        return self.game_project_title

    @property
    def R_Panda3dVersion(self) -> str: 
        return self.panda3d_version
    
    @property 
    def R_Author(self) -> str: 
        return self.game_author
    
    @property
    def R_Company(self) -> str: 
        return self.game_company

    @property 
    def R_Website(self) -> str:
        return self.game_website

    ########################
    # In-Game Attributes (Score, etc.)
    ########################

    @property 
    def RC_collectible_coins(self) -> int: 
        return self.ingame_collectible_coins

    @RC_collectible_coins.setter
    def RC_collectible_coins(self, new_number_of_coins): 
        self.ingame_collectible_coins = new_number_of_coins
        return self.ingame_collectible_coins

    @RC_collectible_coins.deleter
    def RC_collectible_coins(self): 
        self.ingame_collectible_coins = 0
        return self.ingame_collectible_coins

    ########################
    # Menu Attributes
    ########################

    @property
    def RC_game_paused(self): 
        return self.menu_pause

    @RC_game_paused.setter
    def RC_game_paused(self, value): 
        if value is False: 
            self.menu_pause = False 
        elif value is True:
            self.menu_pause = True

    @property
    def RC_OnScreenText_objects(self) -> list: 
        return self.menu_OnScreenText_objects

    @RC_OnScreenText_objects.setter
    def RC_OnScreenText_objects(self, item) -> list: 
        self.menu_OnScreenText_objects.append(item)

    @property 
    def RC_settings_fog(self) -> bool: 
        return self.menu_settings_fog

    @RC_settings_fog.setter 
    def RC_settings_fog(self, boolean_value) -> bool: 
        self.menu_settings_fog = boolean_value
        return self.menu_settings_fog


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
