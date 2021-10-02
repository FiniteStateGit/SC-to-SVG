# SC-to-SVG

Convert Open 3D Engine Script Canvas graphs to SVG images.

## Python Requirements

Python >= 3.6
Jinja2
Graphviz

## Usage

Run `sc_diagram.py` in the same directory as the `basic.scriptcanvas` file. 
The script saves an intermediate Graphviz `.dot` file, `basic.gv`.
The script saves a .svg image of the graph as `basic.gv.svg`. 
