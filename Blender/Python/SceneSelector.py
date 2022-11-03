###########################################################################################################################
#                                                                                                                         #
#   ██████╗  ██████╗ ██╗     ██████╗  █████╗ ███╗   ██╗███╗   ██╗██╗██╗   ██╗ █████╗ ████████╗███████╗ ██████╗██╗  ██╗    #
#  ██╔════╝ ██╔═══██╗██║     ██╔══██╗██╔══██╗████╗  ██║████╗  ██║██║╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔════╝██╔════╝██║  ██║    #
#  ██║  ███╗██║   ██║██║     ██║  ██║███████║██╔██╗ ██║██╔██╗ ██║██║ ╚████╔╝ ███████║   ██║   █████╗  ██║     ███████║    #
#  ██║   ██║██║   ██║██║     ██║  ██║██╔══██║██║╚██╗██║██║╚██╗██║██║  ╚██╔╝  ██╔══██║   ██║   ██╔══╝  ██║     ██╔══██║    #
#  ╚██████╔╝╚██████╔╝███████╗██████╔╝██║  ██║██║ ╚████║██║ ╚████║██║   ██║   ██║  ██║   ██║   ███████╗╚██████╗██║  ██║    #
#   ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═     #
#                                                                                                                         #
#         ➡️ Goldanniyatech is a 3D Software Dev & Self-Publishing Studio founded by Yoann AMAR ASSOULINE in 2021        #
#                                                                                                                         #
# Blender Scene Selector                                                                                                  #
#                                                                                                                         #
###########################################################################################################################/

# TO DO
# * change view layers in one click (small buttons below the scene button)

bl_info = {
    "name": "Blender Scene Selector", 
    "blender": (2, 80, 0), 
    "category": "Object", 
    "author": "Yoann AMAR ASSOULINE (Goldanniyatech)",
}

# Built-in Imports
import os 
import platform 

# Blender import
try: 
    import bpy
except ImportError: 
    print('You must run this Python script from the Blender Software')
    os._exit(0)


class SceneSelector(bpy.types.Operator): 
    """ Class used to select a scene based on its name """ 
    
    bl_idname = "wm.scene_selector"
    bl_label = "Scene Selector Operator" 
    
    # Operator Properties (bpy.props)
    SceneName: bpy.props.StringProperty(name="Scene Name Value")
    
    def __init__ (self):  
        pass 
          
    def execute(self, context): 
        # for scene in bpy.data.scenes
        #   print(scene.name)
        bpy.context.window.scene=bpy.data.scenes[self.SceneName] 

        return {'FINISHED'}

class BlenderScenesPanel(bpy.types.Panel): 
    """ Creating the Scene Selector Panel """
    
    bl_label = "Blender Scene Selector" 
    bl_idname = "OBJECT_PT_BlenderScenes"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI" 
    bl_category = "Scene Selector" 
    
    def draw(self, context): 
        layout = self.layout  
        
        for scene in bpy.data.scenes: 
            
            test = layout.operator ("wm.scene_selector", text=scene.name, icon="SCENE")
            
            test.SceneName = scene.name

def register(): 
    bpy.utils.register_class(SceneSelector)
    bpy.utils.register_class(BlenderScenesPanel) 
    
def unregister(): 
    bpy.utils.unregister_class(BlenderScenesPanel) 
    bpy.utils.unregister_class(SceneSelector)
    
if __name__ == "__main__": 
    register()