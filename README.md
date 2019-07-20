# RunwayML plug-in for GIMP

This plug-in allows you to use GIMP as a segmentation map editor for [RunwayML](http://runwayml.com/).

Just start a model that uses a segmentation map as an input in Runway and select `Filter > Runway` in GIMP to process the currently selected layer.

## Installation

Put the `runway.py` script into the GIMP plug-ins folder (create the folder if it does not exist):

* macOS: `$HOME/Library/Application Support/GIMP/2.10/plug-ins`
* Windows: `$HOME/AppData/Roaming/GIMP/2.10/plug-ins`
* Linux: `$HOME/.config/GIMP/2.10/plug-ins`
