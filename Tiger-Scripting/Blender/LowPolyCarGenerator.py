# ***********************************************************************
# *                                                                     *
# *                       Low Poly Car Generator                        *
# *                                                                     *
# * Description:                                                        * 
# * This generator was made for a mini-game in the
# * Golden Project and for learning purposes. 
# *  Feel free to use it for any project, in any 
# *  game engine
# *
# * Features:                                                           *
# * ->                                                                  *
# *                                                                     *
# * To Do                                                               *
# * ->                                                                  *
# *                                                                     *
# * Known Bugs:                                                         *
# *  -None. Please reach out if you find one                            *
# *                                                                     *
# *              Yoann AMAR ASSOULINE @ GOLDANNIYATECH                  *
#************************************************************************


import bpy
from random import random 


# **************************************
# Global Variables 

CarCount = 1 #Number of car generated in a row
CarExport_FBX = False #Exporting format: FBX

GeneratorTimeDelay = 0 #increase for a visual generator
# https://docs.blender.org/api/blender2.8/bpy.app.timers.html


CarMesh_1 = bpy.ops.mesh.primitive_cube_add(location=(0, 0, 0))

#CarMesh_1.object.modifier_add(type='MIRROR')
