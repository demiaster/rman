# rman

First project using Python API for RenderManProServer.

The aim is to create a believable wall pin geometry and render it with proper shading and lighting.

## Repository structure

* `docs`: the .tex file is a breakdown of the modeling and shading process. In the same folder you can also find the final image produced by the main script.
* `shaders`: contains all the shader for the project.
* `textures`: all the textures for the project.

## Requirements

Tested on: RenderManProServer (python engine 2.7).

## Execute

* Dive in the shaders folder and compile using the following commands:
    - `oslc *.osl`: will compile the new generation shaders.
    - `shader *.sl`: will compile the old .sl shaders.
    
* Open RenderMan visualization program `it`
* Execute the `scene.py` script by typing in the terminal:
    - `./scene.py`: it executes the python scripts and produces the RIB file
    - `render scene.rib`: it will send and start rendering the image in the previously opened `it` program.
    
## Examples

![alt text](https://github.com/demiaster/rman/blob/master/final_images/scene_1.png "Red and Blue Pins")
![alt text](https://github.com/demiaster/rman/blob/master/final_images/scene_2.png "Red and Green Pins")
