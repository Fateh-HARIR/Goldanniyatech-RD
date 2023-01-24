*--------------------------------------------------------------------------------*
  *                Yoann AMAR ASSOULINE (GOLDANNIYATECH)                          *
  *                                                                               *
  *                       3D Poster Generator                                     *  
  *-------------------------------------------------------------------------------*/

try (DestroyDialog FolderSelectorRollout)catch() --> destroy a rollout called "rol_ObjectGen" (a previous version). 

persistent global PicGenPath
if (PicGenPath == undefined) do ( PicGenPath = "" + "Games\\" ) 

/*  Resources + Items Path */ --FBX Prefix should be added later. 
global LV0Path = "D:\Yoann\TestFolder\\"   --> Default Unity 3D Resources Path
global LV1Path = ""
global LV2Path = ""
global LV3Path = ""
persistent global FullPath = (LV0Path + LV1Path + LV2Path + LV3Path) --> Path used to generate things. 

--> .Max File Path System
global MAXLV0Path = "E:\Yoann\TestFolder" --> Default .Max Path
global MAXLV1Path = ""
global MAXLV2Path = ""
global MAXLV3Path = ""
global MAXFullPath = (MaxLV0Path + MAXLV1Path + MAXLV2Path + MAXLV3Path) --> Path for the Data Import system.

/* Describe the path level (2, 3...)   /!\ Might be deprecated /!\   */
global LV2State = false
global LV3State = false


-->  Resources Path (Unity 3D, FBX Files + Textures)
global FBXLv0 = "E:\Yoann\TestFolder\\"   --> Default Unity 3D Resources Path
global FBXLv1 = ""
global FBXLv2 = ""
global FBXLv3 = ""
global FBXLv4 = ""
persistent global FBXFullPath = (FBXLv0 + FBXLv1 + FBXLv2 + FBXLv3) --> Path used to generate things. 

--> .Max Path 
global MaxLv0 = "E:\Yoann\TestFolder" --> Default .Max Path
global MaxLv1 = ""
global MaxLv2 = ""
global MaxLv3 = ""
persistent global MaxFullPath = (MaxLv0 + MaxLv1 + MaxLv2 + MaxLv3) --> Path for the Data Import system.

--> Empty Photoshop Textures
global PsPath = ""

rollout FolderSelectorRollout "Folder Selector 1"
(
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

	group "Folders"
	(
		button ApplyMaterial "Apply existing material"
		button CreateMaterial "create new material (by name)"
		button DestroyMaterial "Destroy material"
		label CurrentPath  ""
		label CurrentPath2  ""
	)

	label confidential "Confidential Project"
	label confidentialProject "© AMAR Yoann. All Rights Reserved" 




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



	/*--------------------->     DDL Selection (Data Settings)     <------------------------------------*/
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


	on DestroyMaterial pressed do  
	(   
		CurrentPath.text = FBXFullPath
		CurrentPath2.text = FullPath
		FullPathLabel.text = FBXFullPath
	)
)
createDialog FolderSelectorRollout height:500 width:430 pos:[40,505]  