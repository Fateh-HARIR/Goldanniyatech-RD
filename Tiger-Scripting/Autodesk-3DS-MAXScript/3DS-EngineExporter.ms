 /*------------------------------------------------------------------------------------*
  *                        Yoann AMAR ASSOULINE (Goldanniyatech)                       *
  *                                Game Engine Exporter                                *
  *                                                                                    *
  * ♦️ Features:                                                                        *
  *         - Item Generator : -  Pictures (Auto Size for X and Y) 
  *							    - @Geometry-based instances, 
  *							  	 - (Planned) Box (Auto Size for X, Y and Z)
  *					        	 - (Planned) Book (Auto Size)
  *						     	 - (Planned) @Complex Geometry-based generator (Train, car, buildings, etc.)    
  *
  *-------------------------------------------------------------------------*/
  
try (DestroyDialog rol_ObjectGen)catch() --> destroy a rolelout called "rol_ObjectGen" (a previous version). 

persistent global ProjectPath 
if (ProjectPath == undefined) do ( ProjectPath = "D:\Yoann\TestFolder\\" ) 

/*  Resources + Items Path */ --FBX Prefix should be added later. 
global LV0Path = ProjectPath  --> Default Unity 3D Resources Path
global LV1Path = ""
global LV2Path = "" 
global LV3Path = ""
persistent global FullPath = (LV0Path + LV1Path + LV2Path + LV3Path) --> Path used to generate things. 

--> .Max File Path System
global MAXLV0Path = "D:\Yoann\TestFolder\\" --> Default .Max Path
global MAXLV1Path = ""
global MAXLV2Path = ""
global MAXLV3Path = ""
global MAXFullPath = (MaxLV0Path + MAXLV1Path + MAXLV2Path + MAXLV3Path) --> Path for the Data Import system.

--> Status on the File System & Level
global LV1State = false 
global LV2State = false
global LV3State = false

global MaxPath = true

rollout rol_ObjectGen "Object Generator"
(  
	
	/*----------------->    User Interface ::: Data Settings   <-----------------*/
	label confidential "Golden Confidential Generator 4.0"
	group "MAX Data Import Settings" --> Use this path to open/ Merge or Save .Max files. 
	(
		label MAXFullPath "(currently unused) .Max Full Path" align:#left
		dropdownlist MAXddl_Lv1 items:#("") across:4
		dropdownlist MAXddl_Lv2 items:#("")
		dropdownlist MAXddl_Lv3 items:#("")
		dropdownlist MAXddl_Lv4 items:#("")
		button MAXSave "Max File Save" across:2 
		button MaxLoad "Max File Load" 
	)
	
	group "FBX Data Export Settings" -- Point out the items Path to the generator.
	(	
		label FullPathLabel FullPath align:#left  
		
		dropdownlist ddl_Lv1 items:#("") offset:[00,0] tooltip:"First Folder" across:4 --width:250 across:3
		dropdownlist ddl_Lv2  items:#("")  offset:[00,0]   
		dropdownlist ddl_Lv3  items:#("")  offset:[00,0] 
		dropdownlist FBXddl_Lv4  items:#("")  offset:[00,0] 
	 
		label ProgressBarCurrentFolderLabel "Current Folder" tooltip:"bonjour" across:4
		progressbar ProgressBar1 "current" value:100 color:green
		label ProgressBarAllFoldersLabel "?.? All Folders" 
		progressbar ProgressBar2 "" value:100 color:yellow
	)   
	
	group "Miscellaneous ByPasses"	/*----------------->    User Interface ::: Miscellaneous   <-----------------*/
	(
		button ApplyMaterial "Apply Material"  across:3 --> Path based on "FullPath" and texture's name based on selected 3D Model name.  <--
		button ExportSelected "Export Selected (Not ready)"		
		button ExportAll "Export All (Not ready)"
	)
		label UnusedLabelMasterKey ""
		button ObjectGenButton "=-->  MasterKey  <--="   
	group "Settings" 	/*----------------->    User Interface ::: Generator Settings   <-----------------*/
	( 
		checkbox GenSettings_Export "Export FBX" across:3 checked:true
		checkbox GenSettings_Delete "Delete FBX 3D Models" checked:true
		checkbox GenSettings_AllFolders "All Folders (Current DDL)"
		checkbox GenSettings_TexChildByWord "Texture (Child) By First Word" across:2
		checkbox GenSettings_TexChildByName "Texture (Child) By Full Name"
	)
	group "Texture Option"
	(
		checkbox GenSettings_JPG "Load .jpg Files" across:3 checked:true 
		checkbox GenSettings_PNG "Load .png Files"  checked:true 
		checkbox GenSettings_PSD "Load .psd Files"  checked:true 
		label RightTabLabel "" across:3 -- Unused Label
		checkbox GenSettings_Transparency "Enable .png Transparency"
		label LeftTabLabel ""  -- Unused Label
	)
	group "Object Type"
	( 
		radiobuttons ObjectGenerated_Rad labels:#("Picture (Media)", "Box (Food)", "@Geometry (Objects)") align:#left 
	)
	
	label confidential2 "AMAR ASSOULINE Yoann" 
	label confidential3 " 2022"
	
	
		
   /*-----------------------------------------------------------------------------*
	*------------>                      FONCTIONS                      <-------------*
     *------------------------------------------------------------------------------*/ 
	
	/*--->   fn to update the path anywhere   <----*/
	function UpdatePath ddl1 ddl2 ddl3 ddl4 =
	( 	global LV1Path = ""
		global LV2Path = ""
		global LV3Path = ""
		global LV4Path = ""  
     
		--> Check if DropDownList[].selected exist and retrieve the value <--
		if (ddl1 != "") do (global LV1Path = ddl1 + "\\") 
		if (ddl2 != "") do (global LV2Path = ddl2 + "\\")  
		if (ddl3 != "") do (global LV3Path = ddl3 + "\\")
		if (ddl4 != "") do (global LV4Path = ddl4 + "\\")
		   
		
		global FullPath = LV0Path + LV1Path + LV2Path + LV3Path + LV4Path
		FullPathLabel.text = FullPath -- User Interface Label Update 
	) /*****************     END of function     ****************/
	
	
	/* -->  fn to (loop and) search through the directory and find any folder  <--*/
	function DLLSearchDirectory nextDDL CurrentPath = -- /!\ "CurrentPath" in test. Before, nothing else than "nextDDL" was here
	(	nextDDL.items = #()  -- Clear array.
		WantedFolders = getDirectories (CurrentPath + "\*")
		for i = 1 to (WantedFolders.count) do 
		( 	
			f = replace WantedFolders[i] 1 (CurrentPath.count) ""
			f = replace f f.count 1 ""
			nextDDL.items = append nextDDL.items f 
			if (f == "Materials") do -- Remove generated UNITY 3D "Materials" folder from list. 
			( 	nextDDL.items = deleteItem nextDDL.items i		)
		) 
	) /*****************     END of function     ****************/
	 
	 
	 
	/* -->  fn to Apply material to selection  <--*/
	function ApplyMaterialToObject =
	( 	for i = 1 to selection.count do 	 
		(	newmat = StandardMaterial()
			newmat.name = (selection[i].name as string)
			newmat.showInViewport = on			
			selection[i].material = newmat 
			
			--> Check if texture exist in FullPath			
			if (doesfileexist (FullPath+selection[i].name+".psd") == true) do	    GigaMap = bitmaptexture filename:(FullPath+selection[i].name+".psd")
			if (doesfileexist (FullPath+selection[i].name+".png") == true) do 	GigaMap = bitmaptexture filename:(FullPath+selection[i].name+".png")	
			if (doesfileexist (FullPath+selection[i].name+".jpg") == true) do 	GigaMap = bitmaptexture filename:(FullPath+selection[i].name+".jpg")	  
			
			newmat.diffusemap = GigaMap		
			newmat.diffusemap.name = selection[i].name    
		)
	) /*****************     END OF function     ****************/
	
	
	
	
	/*--------------------------------------------------->     DDL Selection (Data Settings)     <---------------------------------------------------*/
	on rol_ObjectGen open do 	 /*  --->   Rollout StartUp  Settings  (Generating DDL1)  <--- */
	( 	DLLSearchDirectory (ddl_Lv1)  (FullPath)	
		UpdatePath (ddl_Lv1.selected) ("") ("") ("") )
	
	/*--------------------------------------> MAX DDL <-------------------------------*/
	 
		
		
	/*---------------------------------------> Generator DDL <---------------------------------------*/
	on ddl_Lv1 selected selection do 
	(   UpdatePath (ddl_Lv1.selected) ("") (  "" ) ("") /* Function to update Path & Label*/ 
		DLLSearchDirectory (ddl_Lv2)   (FullPath)   )/* Function to search through the directory */ 

	on ddl_Lv2 selected selection do   
	( 	UpdatePath (ddl_Lv1.selected) (ddl_Lv2.selected) (  "" ) ("")  
		DLLSearchDirectory (ddl_Lv3)  (FullPath) )
	 
	on ddl_Lv3 selected selection do  
	(    UpdatePath (ddl_Lv1.selected) (ddl_Lv2.selected) ( ddl_Lv3.selected) ("")  
		DLLSearchDirectory (FBXddl_Lv4)  (FullPath))
 
	on ddl_Lv4 selected selection do  
	(    UpdatePath (ddl_Lv1.selected) (ddl_Lv2.selected) ( ddl_Lv3.selected) (FBXddl_Lv3.selected)  )


   /***********************************************************************
	************************      BYPASSES      *****************************/ 
	on ApplyMaterial pressed do 	(   ApplyMaterialToObject()    )
	
	
	
	
	/*****************************************************************************************************
	 **********************      GENERATOR      ***********************************************************/
	on ObjectGenButton pressed do  
	(   
		/* ALLFolders Checkbox */
		if (GenSettings_AllFolders.state == true) do 
		(  	if (ddl_LV2.items != undefined) do 
				( if (LV2State == true ) do (ObjectsArray = ddl_LV2.items.count )  )
			if (ddl_LV3.items != undefined) do 
				( if (LV3State == true ) do (ObjectsArray = ddl_LV3.items.count)   ) 
		)
		if (GenSettings_AllFolders.state == false) do 
			(ObjectsArray  = 1) 
		
		for i=1 to (ObjectsArray) do 
		(
		  print GenSettings_AllFolders.state
		  print ObjectsArray
			
		 /* AllFolders Path */
		if (GenSettings_AllFolders.state == true) do 
		(	
			if (LV2State == true) do 
			( 	ddl_LV2.selection = i
				persistent global LV2Path = ddl_Lv2.selected + "\\"
				persistent global FullPath = (LV0Path + LV1Path + LV2Path + LV3Path) 
			) 
			if (LV3State == true) do 
			( 	ddl_LV3.selection = i
				persistent global LV3Path = ddl_Lv3.selected + "\\"
				persistent global FullPath = (LV0Path + LV1Path + LV2Path + LV3Path)  
			)
		)
		  
		---->    Search Textures in  FullPath/*     <----
		jpgFiles = getFiles (FullPath + "*.jpg")
		pngFiles = getFiles (FullPath + "*.png") 
		psdFiles = getFiles (FullPath + "*.psd")
		TotalFiles = jpgFiles + pngFiles + psdFiles  
		 
		---->    Remove old  FullPath/*.FBX  Files    <----
		if (GenSettings_Delete.state == true) do 
		(	OldFBX  = getFiles (FullPath + "*.FBX") 
			for b = 1 to (OldFBX.count) do 
			(	deleteFile OldFBX[b]      )		       )
		 
			
		for f = 1 to (TotalFiles.count) do 
		(   			
			ProgressBar1.value = 100.0*f/TotalFiles.count
			
			/* RADIOBUTTONS CHOICE */
			if (ObjectGenerated_Rad.state == 1) do 
			( 	Box length:0.4 width:20 height:20 
				select $Box001  
				max modify mode 
				modPanel.addModToSelection (Uvwmap ()) 
				$.modifiers[#UVW_Map].maptype = 4 
				MainObject = "Box001"
			)
			
			if (ObjectGenerated_Rad.state == 3) do 
			( 	if (LV2State == true) do (MainObject = ("@"+ddl_LV2.selected) as string )
				if (LV3State == true ) do (MainObject = ("@"+ddl_LV3.selected) as string )
			)
			
			ObjectStored = execute (" select $'"+MainObject+"'")    
			actionMan.executeAction 0 "40180"  -- select children 
			actionMan.executeAction 0 "40180"    
			
			
			if (ObjectGenerated_Rad.state == 3) do /* Clone @Geometry Object (to keep the same 3D model) */
			( 	maxOps.cloneNodes $ expandHierarchy:false cloneType:#copy newNodes:&nnl /*#nodialog */
				select nnl
				nnl.name = uniqueName "This" numDigits:3
			)
			 
			actionMan.executeAction 0 "40193"  	
			move $ [0,f*10,0]   
			 
			ab = TotalFiles[f] 
			$.name =  substring  ab (FullPath.count+1) (ab.count-FullPath.count-4)   
				
			---->   Apply Material    <----
			newmat = StandardMaterial()
			newmat.showInViewport = on 
			GigaMap = bitmaptexture filename:TotalFiles[f] 
			$.material = newmat  
			newmat.diffusemap = GigaMap	
			newmat.diffusemap.name = $.name
			
			/*
			if (GenSettings_TexChildByWord.state == true) do 
			(
				testingPath =  getDirectories ( LV0Path  + LV1Path + "\*")
				print testingPath.count
				print $
				
				
				AncestorName = $.name as string 
				print AncestorName
				AncestorNameWordPos = findString AncestorName " "  
				AncestorNameWord = substring AncestorName 1 AncestorNameWordPos
				print AncestorNameFirstWord 
			--	actionMan.executeAction 0 "40180"  -- select children (ALL) 
				print selection.count/*
				for t = 1 in selection.count do 
				(
					
				)

				)*/ 
			--actionMan.executeAction 0 "40193"  	
			--actionMan.executeAction 0 "40193"  	
				
							
			
			if (ObjectGenerated_Rad.state == 1) do 
			(   ---->    Picture Scale    <----
				GigaMapBM = GigaMap.bitmap
				GigaMapBMY = GigaMapBM.height*0.001 as float 
				GigaMapBMX = (GigaMapBM.width)*0.001 as float  
				scale selection [GigaMapBMX, 1, GigaMapBMY]  
			)
			
			
			---->    Export to FullPath (.FBX)    <----
			FBXSavePath = (FullPath + $.name ) 
			actionMan.executeAction 0 "40180"  -- select children  
			if (GenSettings_Export.state == true) do 		(exportFile FBXSavePath  #noPrompt selectedOnly:True using:FBXEXP )
			if (GenSettings_Delete.state == true ) do 		(max delete) 
			
		) 
	)
	)
	
	
) ---->    END of Rollout    <----
createDialog rol_ObjectGen height:900 width:500 pos:[40,505]
