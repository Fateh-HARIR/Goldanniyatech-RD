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
# Render Quick Configurator                                                                                               #
#                                                                                                                         #
###########################################################################################################################/

bl_info = {
    "name": "Render Configurator",
    "blender": (2, 80, 0), 
    "category": "Render", 
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

# Add-on Variables
AddonDict = {
    'DebugMode' : True 
}


class RenderOperator(bpy.types.Operator): 
    """ Operator to generate a single Render based on multiple parameters """ 
    
    bl_idname = "wm.render_operator"
    bl_label = "Render Operator" 
    
    def __init__(self): 
        pass
    
    def execute(self, context): 
        bpy.ops.render.render()
        return {'FINISHED'}
    

class ViewportRenderOperator(bpy.types.Operator): 
    """ Operator to take a Viewport screenshot based on multiple parameters """ 
    
    bl_idname = "wm.openglrender_operator"
    bl_label = "OpenGL Render Operator" 
    
    def __init__(self): 
        pass
    
    def execute(self, context): 
        bpy.ops.render.opengl()
        return {'FINISHED'}
    

class RenderConfiguratorPanel(bpy.types.Panel): 
    """ Main Panel of the Render Configurator Add-on """ 
    
    bl_idname = "VIEW3D_PT_RenderQuickSettings_Panel"
    bl_label = "Render Quick Settings"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category="Render"
    
    def draw(self, context): 
        
        layout = self.layout
        layout.label(text="Render Quick Settings")
        
        layout.separator(factor=1.5)
 
        row_A = layout.row() 
        row_A.label(text="Render Resolution")
        row_A.operator("object.select_random", text="Render", icon="IMPORT")
        
        layout.prop(context.scene.render, 'engine')
        
        layout.operator("wm.render_operator", text="Generate Render", icon="IMPORT")

        layout.operator("wm.openglrender_operator", text="Render Viewport", icon="IMPORT")
        
# Classes tuple
RenderClasses = (
        RenderConfiguratorPanel,
        RenderOperator, 
        ViewportRenderOperator
)

def register(): 
     
    for cls in RenderClasses: 
        bpy.utils.register_class(cls)
        
def unregister(): 
     
    for cls in reversed(RenderClasses): 
        bpy.utils.unregister_class(cls)

if __name__ == "__main__": 
    register() 
