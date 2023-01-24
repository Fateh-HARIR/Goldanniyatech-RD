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
# Game Engine Mesh Exporter                                                                                               #
#                                                                                                                         #
###########################################################################################################################/

bl_info = {
    "name": "Game Engine Exporter", 
    "blender": (2, 80, 0), 
    "category": "Object", 
    "author": "Yoann AMAR ASSOULINE (Goldanniyatech)",
}

# Built-in imports
import os 
import sys
import platform
try: 
    import pathlib
except ImportError: 
    print('⚠ Please update your Blender version to update its embedded Python interpreter')
    print('Current Python version: ' + sys.version)

# Blender import
try: 
    import bpy
except ImportError: 
    print('⚠ You must run this Python script from the Blender Software')
    os._exit(0)

# Add-on Data Dictionary
Addon_Data = dict(
    Exporter_Version = 1.0,
    Exporter_DebugMode = True # Debug Mode uses print and other built-in functions to display useful data
)

# Exporting Data Dictionary 
Exporting_Data = dict(
    ProjectName = "Blender Default Project",
    ProjectPath = "C:\\", # Be careful about access restriction
    ProjectFilename = 'TestFile', # Should not include any file format extension
    GameEngine = 'Unreal', # 'Unity' | 'Godot'
    ExportFormat = 'FBX',  # 'BLEND' | 'glTF' 
    ExportContext = 'Game' # 'Movie' 
)


class Export_Core (bpy.types.Operator): 
    """
    Main class to export a mesh from Blender to a Game Engine
    """
    
    bl_idname = "wm.game_engine_exporter"
    bl_label = "Operator"
    
    def __init__ (self): 
        # Instance variables 
        self.ProjectPath = Exporting_Data["ProjectPath"] + "/" + Exporting_Data["ProjectFilename"] + "." + Exporting_Data["ExportFormat"]
    
        self.GameEngine = Exporting_Data["GameEngine"]
        self.ExportFormat = Exporting_Data["ExportFormat"]
        
    def SearchingEngines(self): 
        pass
    
    def execute(self, context): 
        
        print(Exporting_Data["ProjectPath"])
        
        if (Addon_Data["Exporter_DebugMode"] == True): 
            print("Exporting Meshes") 
        
        if self.ExportFormat == 'FBX': 
            
            if (Addon_Data["Exporter_DebugMode"] == True): print("Exporting in FBX Format")
            
            try: 
                bpy.ops.export_scene.fbx(
                    filepath=self.ProjectPath
                    )
            except Exception as PermiError: 
                if (Addon_Data["Exporter_DebugMode"] == True): print("Exception")
                

            
        return {'FINISHED'}
        
            
class Debug_Printer():
    """
    Class used to print critical information when the global variable DebugMode is True
    """
    
    def __init__ (self, context): 
        self.Path = "test"
    
    def Debug(self, context):
        if (Addon_Data["Exporter_DebugMode"] == True): 
    
            # Clear the interpreter console
            if (platform.system() == "Windows"): 
                os.system('cls')
            else:
                os.system('clear')
            
            print("Hi there, " + os.getlogin() + "! The DebugMode has been activated!")
        
            print("★ Operating System: ")
        
            print("★ Blender Version: ", bpy.app.version_string)
        
            print("Project Path", Export_Core.ProjectPath)
            
            print("Exporter_Core Game Engine: ", Export_Core.GameEngine)
            
            
class Exporter_CorePanel(bpy.types.Panel): 
    """
    Main Blender Panel (GUI) to use the exporter. It is found in the Sidebar (toggle it with the N key on your keyboard)
    """
    
    bl_idname = "GameEngineExporter"
    bl_label = 'Game Engine Exporter'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "3D Exporter"
                    
    def draw(self, context): 
        
        layout = self.layout 
    
        # Panel Header     
        if (Addon_Data["Exporter_DebugMode"] == True): layout.label(icon="ERROR", text='★ Debug Mode Enabled ★')
        
        layout.label(icon="INFO", text='Add-on Version ' + str(Addon_Data["Exporter_Version"]))
    
        layout.separator(factor=1.0)
                
        # Panel Selection Tools
        box = layout.box() 
        box.label(text="Selection Tools")
        box.operator("object.select_all").action = 'TOGGLE'
        row = box.row()
        row.operator("object.select_all").action = 'INVERT'
        row.operator("object.select_random")
        
        
        row1 = layout.row() 
        row1.label(text="Exporting Folder: ")
        row1.operator("object.select_random", text="Select Path", icon="IMPORT")
            
        layout.prop(context.scene.render, 'engine')
        
        layout.separator(factor=1.0)
        
        #layout.operator("object.select_random", text="Export Meshes")
                
        column1 = layout.column() 
        column1.label (icon="FILE_TICK", text="Exporter Status: AWAITS")
        
        # Exporting Button (calling the Export_Core Class)
        layout.operator(Export_Core.bl_idname, text="Export Meshes")
            
        
# Add-on register & unregister classes 

def register(): 
    bpy.utils.register_class(Export_Core)
    bpy.utils.register_class(Exporter_CorePanel)
    
    # Register the entire module 
    #bpy.utils.register_module(__name__)
     
    if (Addon_Data["Exporter_DebugMode"] == True): 
        print("Registered")
        
def unregister(): 
    bpy.utils.unregister_class(Exporter_CorePanel)
    bpy.utils.unregister_class(Export_Core)
     
    #bpy.utils.unregister_module(__name__)
        
    if (Addon_Data["Exporter_DebugMode"] == True): 
        print("Unregistered")   
    
    
# Running the script by checking if it's the main python script
if __name__ == '__main__': 
    
    register()
    