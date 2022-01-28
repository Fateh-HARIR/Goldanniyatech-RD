#
#   ██████╗  ██████╗ ██╗     ██████╗  █████╗ ███╗   ██╗███╗   ██╗██╗██╗   ██╗ █████╗ ████████╗███████╗ ██████╗██╗  ██╗
#  ██╔════╝ ██╔═══██╗██║     ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██║╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║
#  ██║  ███╗██║   ██║██║     ██║  ██║███████║██╔██╗ ██║██╔██╗ ██║██║ ╚████╔╝ ███████║   ██║   █████╗  ██║     ███████║
#  ██║   ██║██║   ██║██║     ██║  ██║██╔══██║██║╚██╗██║██║╚██╗██║██║  ╚██╔╝  ██╔══██║   ██║   ██╔══╝  ██║     ██╔══██║
#  ╚██████╔╝╚██████╔╝███████╗██████╔╝██║  ██║██║ ╚████║██║ ╚████║██║   ██║   ██║  ██║   ██║   ███████╗╚██████╗██║  ██║
#   ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝                                                                                                           
#
#                              🎮 🧪  GOLDANNIYATECH Research & Development Project  🧪 🎮
#                                                   🐼 Panda 3D Prototypes
#
#                                                     🌇 SUNSET PROJECT 🌇
#
#                                                   By Yoann AMAR ASSOULINE

# Import Panda3D modules
from direct.showbase.ShowBase import ShowBase 
from panda3d.core import WindowProperties 

# Import Sunset Project Modules 

# Global Variables
DevMode = ["DEBUG", "TEST", "RELEASE"]

WindowSize_240p  =  320,  240
WindowSize_360p  =  480,  360
WindowSize_480p  =  720,  480 # SD  
WindowSize_720p  = 1280,  720 # HD or HD Ready
WindowSize_1080p = 1920, 1080 # FHD or Full HD 
WindowSize_1440p = 2560, 1440 # QHD or Quad HD
WindowSize_2160p = 3840, 2160 # UHD or UltraHD 

# Main Sunset Project Class
class SunsetPanda3DApp (ShowBase): 

    def __init__(self): 
        ShowBase.__init__(self)

        #Windows Size
        properties = WindowProperties() 
        properties.setSize(WindowSize_720p)
        self.win.requestProperties (properties)


Panda3DApp = SunsetPanda3DApp()
Panda3DApp.run()
