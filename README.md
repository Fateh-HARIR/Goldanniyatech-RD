[//]: # (Yoann AMAR ASSOULINE - GOLDANNIYATECH) 

# 3D Game Development Research Overview

⚠️ *Note: this repository is currently under heavy development and these projects or mini-games might not work (at all). Only a Release is intended to be used.*

This **3D Game Development Research Laboratory** is a collection of open source mini-games made with various Game Engines & 2D/ 3D software, mainly for research purposes. I only use tools that are under heavy development or *at least* under maintenance in the past two years.

Of course, feel free to learn from or re-use this content in any of your (commercial) projects, as long as you properly credit me (Yoann AMAR ASSOULINE @Goldanniyatech). Each project has been tested with the *version* mentioned below, and should be working right off the bat.

## Technical Stack
Here's the full list of every software, programming language & graphics software I've used. Note that everything is entirely made by myself from scratch, from programming scripts to 3D asset (modeling, texturing, animations...). 

🌀 **Programming Languages**:  C++ • C# • Java • Python

🌀 **2D/ 3D Graphics**: Autodesk 3DS Max 2023 • Autodesk Maya 2023 • Blender 3.3

🌀 **Game Engines**: Panda3D 1.10.12 • Unity 2021.3 • Unreal Engine 5.1


## Projects Overview

### **Kobra-Scripts** (Scripting Project)
A set of Python scripts to improve productivity. It's currently only for Blender but the goal is to expand the project to write the same scripts for 3DS Max, Maya and Blender. 

:x: Blender Game Engine Exporter

:x: LowPoly Car Generator

:x: Model Statistics

:white_check_mark: Render Configurator

:white_check_mark: Scene Selector

### :x: **Royal Palace** (Mini-Game)

**Royal Palace** is a mini-game built in Panda3D (in Python) from scratch, with 3D models & texture made from scratch in Blender (some tweaks have been made for Adobe Photoshop).
The game itself revolves around a small family living in a castle & collecting coins all day long. 

<!-- 
Dev Status: the **Royal Palace mini-game project** is finished and only under maintenance, with some tweaks from time to time. 
-->

Note: for **Panda3D**, Each model was made with Blender (texture included, painted with Blender tools & tweaked with Photoshop when needed) and firstly exported in gltf 2.0. 
Then, the panda3d-gltf converter [https://github.com/Moguri/panda3d-gltf], installed with PIP, can help to convert .gltf to .bam. by using the cmd (gltf2bam source.gltf output.bam)
It is definitely not the most effective way, especially when you compare that process with **Unreal Engine** or **Unity**, but it works! 


<!-- ### **Unity** -->

<!-- ### **Unreal Engine** -->
