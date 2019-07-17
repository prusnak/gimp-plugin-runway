#!/usr/bin/env python2
from gimpfu import register, main, gimp, RGB_IMAGE, NORMAL_MODE, pdb
import base64, os, tempfile
import json, urllib2

def python_runway(img, layer):
    if not layer.is_rgb:
        raise ValueError("Expected RGB layer")
    # because pdb cannot save to a buffer, we have to use a temporary file instead
    f = tempfile.NamedTemporaryFile(suffix=".png", delete=False)
    pdb.file_png_save(img, layer, f.name, f.name, 0, 9, 0, 0, 0, 0, 0)
    # convert data from file to base64 encoded bytes
    data = open(f.name, "rb").read()
    b64 = base64.b64encode(data)
    os.unlink(f.name)
    # send data to Runway via a POST request
    data = json.dumps({"semantic_map": b64})
    req = urllib2.Request("http://localhost:8000/query", data, {"Content-Type": "application/json"})
    f = urllib2.urlopen(req)
    resp = json.loads(f.read())
    f.close()
    # save result to a temporary file, because pdb cannot load from a buffer
    jpg = base64.b64decode(resp["output"][22:])
    f = tempfile.NamedTemporaryFile(suffix=".jpg", delete=False)
    open(f.name, "wb").write(jpg)
    # open the temp file
    image = pdb.gimp_file_load(f.name, f.name)
    # copy the first layer to clipboard
    pdb.gimp_edit_copy(image.layers[0])
    os.unlink(f.name)
    # paste clipboard contents as a floating selection
    floating = pdb.gimp_edit_paste(layer, 0)
    floating.name = layer.name + " [Runway]"

register(
    "python_fu_runway",
    "Process the selected layer in Runway",
    "Process the selected layer in Runway",
    "Pavol Rusnak",
    "MIT License",
    "2019",
    "<Image>/Filters/Runway...",
    "RGB*",
    [],
    [],
    python_runway)

main()
