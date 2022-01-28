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
#                                                   By Yoann AMAR ASSOULINE
#
#
#    ⭐ Visual Studio Code Instructions ⭐
# ➡️ Install Python Microsoft Extension
# ➡️ Select the interpreter (bottom left) from Panda3D Folder (Panda3D\python\python.exe)
# ➡️ Check if you can import the Panda3D direct module:
# ➡️ from direct.showbase.ShowBase import ShowBase 

from math import pi, sin, cos 

from direct.showbase.ShowBase import ShowBase 
from direct.task import Task 
from direct.actor.Actor import Actor 
from direct.interval.IntervalGlobal import Sequence
from panda3d.core import Point3 

#print (globals())

class GoldaPanda3DApp (ShowBase) : 

    def __init__(self) : 

        ShowBase.__init__(self) 

        self.disableMouse() 

        #Using error handling to handle personal models made from scratch vs generic models found in Panda3D
        try: 
            self.scene = self.loader.loadModel ("models/TestModel") 
        except: 
            self.scene = self.loader.loadModel ("models/environment") 
        self.scene.reparentTo(self.render) 

        self.scene.setScale(0.4, 0.4, 0.4) 
        self.scene.setPos (4, 1, 1) 

        self.taskMgr.add (self.spinCameraTask, "SpinCameraTask") 

        self.pandaActor = Actor ("models/panda-model", {"walk": "models/panda-walk4"})
        self.pandaActor.setScale (0.005, 0.005, 0.005) 
        self.pandaActor.reparentTo(self.render) 

        self.pandaActor.loop ("walk") 

        posInterval1 = self.pandaActor.posInterval(13, Point3 (0, -10, 0), startPos=Point3(0, 10, 0) )
        posInterval2 = self.pandaActor.posInterval (13, Point3 (0, 10, 0), startPos=Point3(0, 0, 0) )

        hprInterval1 = self.pandaActor.hprInterval (3, Point3 (180, 0, 0), startHpr=Point3 (0, 0, 0) )
        hprInterval2 = self.pandaActor.hprInterval (3, Point3 (0  , 0, 0), startHpr=Point3 (180, 0, 0) )

        self.pandaPace = Sequence (posInterval1, hprInterval1, posInterval2, hprInterval2, name="PandaPace") 
        self.pandaPace.loop() 

    def spinCameraTask (self, task): 
        angleDegrees = task.time * 6.0
        angleRadians = angleDegrees * (pi / 180.0 ) 
        self.camera.setPos (20 * sin(angleRadians), -20 * cos(angleRadians), 3)
        self.camera.setHpr (angleDegrees, 0, 0) 
        return Task.cont 

#Running the application
Panda3DApp = GoldaPanda3DApp() 
Panda3DApp.run() 