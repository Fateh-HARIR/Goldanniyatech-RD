
from panda3d.core import ConfigVariableManager
 
# ConfigVar Variables
R_debug_list_all_configvar = False 
R_load_custom_configvar = False 
R_custom_configvar_path = ""

if R_debug_list_all_configvar is True: print(ConfigVariableManager.getGlobalPtr().listVariables())

class Royal_CustomVar: 

    def __init__ (self): 
        
        if R_load_custom_configvar is True: 
            # loadPrcFile(R_custom_configvar_path + "Royal_Config_Var.prc")
            pass