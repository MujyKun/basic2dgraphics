# Basic 2D Graphic Demo (For CSCI-437)

## Features (What it does)
- Drawing Program
- Select from 16+ Colors (Left)
- Buttons
- Undo and Redo
- Increase or Decrease Drawing Size
- Draw with Shapes (Square, Several Types of Triangles, Polygons, Circles, Several types of Arrows.)
- FPS Counter (Top Left)
- Cursor Position (Top Left)
- Clear entire canvas
- Eraser
- Able to undo a cleared canvas.
- Can deselect from a shape.

## Installation / Local Setup
1) Clone the repository ``git clone https://github.com/MujyKun/basic2dgraphics.git``
2) Go to the repo directory ``cd basic2dgraphics``
3) Running with Python ^3.9 is recommended. 
4) Install requirements with either 
   1) ``pip install -r requirements.txt`` 
      1) If you do not have pip, you can install it with ``python get-pip.py`` or ``python -m ensurepip --upgrade``
   2) If you have poetry you can use ``poetry install``. 
5) Start the program with `python run.py`

### Example Drawing
![Example Drawing](screenshots/no_color_pikachu.png)

### Demonstration
![Drawing Demo](screenshots/demo.gif)

### Blank Canvas
![Black Canvas](screenshots/blank_canvas.png)

### Sample Objects
![Sample Objects](screenshots/sample_objects.png)

## What I learned
   1) Create sub-surfaces so that the creation of certain objects such as buttons do not need to be recreated on every frame.  
   2) How to use relative position of sub-surfaces to detect button presses. 
   3) How to manage the events.
   4) How to manage the frame rate. 
   5) How to process undo and redo tasks. 
   6) How to handle drawing with shapes. 
   7) How to manage color swapping efficiently.
   8) An eraser can just be the background color.
   9) How to render text with a background and process it as a button.
   10) How to use the pygame library. 
   

