# Code128-STL-Generator
Python tool to generate Code128 barcode STL using OpenSCAD

## Overview
This tool generates a 3D model (STL) of a Code128 barcode using Python and OpenSCAD. 
It produces only the black bars extruded from a base plane, ready for 3D printing. 
No bottom subtraction or slots are applied.

## Features
- Input a sring (equal or less than 10 characters) to generate black bars
- Black bars extruded vertically from a base plane
- Configurable unit width, bar length, bar height, and base thickness
- Automatically generates an OpenSCAD file (`.scad`) and STL file (`.stl`)

## Requirements
- Python 3.x
- OpenSCAD installed and CLI accessible (update `OPENSCAD_EXE` in the script if needed)

## Usage
1. Run the script:
2. Enter your string to create a barcode-only stl model
3. Add to your favorate base
4. Change parameters:
OPENSCAD_EXE = r"C:\Program Files\OpenSCAD\openscad.exe" - change to your OpenSCAD install path
UNIT = 0.6                                               - unit mm, define your barcode width
BAR_LENGTH = 25.0                                        - unit mm, define your barcode length
BAR_DEPTH  = 0.5                                         - unit mm, define your barcode depth

## Aplication
Turn your Gym/loyalty/reward card into a customized 3D printing art.

## Printing
I personally use Solidworks/Onshape to design, TinkerCAD/Autodesk Fusion to modify STL model, and Bambu Studio/Bambulb X1C (0.2mm/0.4mm nozele) + AMS to print.  

```bash
python barcode_generator.py
