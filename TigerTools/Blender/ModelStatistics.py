# ****************************************************
# *                                                  *
# *                 Model Statistics                 *
# *                                                  *
# * Features:                                        *
# * -> Counters (Vertices, Edges, Loops, Polys)      *
# *                                                  *
# * To Do                                            *
# * -> Take into account mirror modifiers for stats  *
# *                                                  *
#*****************************************************

import bpy
 
 
# Global Variables 
PolyCount = 0
DebugDisplay = True
DisplayType = ("ascending", "descending") #Tuple


class ModelStatsPanel (bpy.types.Panel):
    bl_label = "Model Statistics"
    bl_idname = "OBJECT_PT_hello"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = "object"
     
    
    def draw(self, context):
        layout = self.layout

        obj = context.object

        row = layout.row()
        row.label(text="Model Statistics", icon='WORLD_DATA')

        row = layout.row()
        row.label(text="Active object is: " + obj.name)
        row = layout.row()
        row.prop(obj, "name")

        row = layout.row()
        row.operator("mesh.primitive_cube_add") 
        
        box = layout.box() 
        row = box.row(align=True) 
        row.label(text="Made by Yoann AMAR ASSOULINE")
        row = box.row() 
        row.label(text="@ Goldanniyatech")
        

def PolyCountChecker(): 
    if DebugDisplay is True: 
        print(" \n \n /!\ Calling PolyCountChecker Function /!\ \n ")
    
    #Loop through all existing objects in the Blender File 
    for obj in bpy.data.objects: 
        #print (obj.name, obj.type) 
        if obj.type == 'MESH': 
            print (obj.name,
                    " Vertices: ", len(obj.data.vertices), 
                    " Edges: ", len(obj.data.edges),
                    " Loops: ", len(obj.data.loops), 
                    " Polygons: ", len(obj.data.polygons) ) 
    
    if DebugDisplay is True: 
        print (" \n \n /!\ PolycountChecker Function end /!\ \n ") 
        
        
         
 
    
def ModelStatsRegister(): 
    bpy.utils.register_class(ModelStatsPanel)
    
def ModelStatsUnregister(): 
    bpy.utils.unregister_class(ModelStatsPanel)
    
if __name__ == "__main__": 
    ModelStatsRegister() 
    
PolyCountChecker()


#for obj in bpy.data.objects:
    #print (obj.name, obj.type) 
#    if obj.type == 'MESH': 
#        print (obj.name)
     
#Check selected object
#if bpy.context.selected_objects != []: 
#    for obj in bpy.context.selected_objects: 
#        print (obj.name, obj.type) 
#        if obj.type == 'MESH': 
#            print (obj.name) 

#loop through all objects in a given scene
#if bpy.context.selected_objects == []: 
#    print ('selected object: ') 
#    for obj in bpy.context.scene.objects: 
#        print(obj.name, obj, obj.type)
#        if obj.type == 'MESH': 
#            print (obj.name)
 