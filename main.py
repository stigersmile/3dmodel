
from __future__ import print_function

import time, threading
import random
import os
import os.path
import sys
import wx


from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Display.SimpleGui import init_display

from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Extend.DataExchange import read_step_file,read_iges_file,write_stl_file, read_stl_file

from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Display.WebGl import x3dom_renderer


# def loadingAnimation(process) :
#     while process.isAlive() :
#         chars = "/—\|" 
#         for char in chars:
#             sys.stdout.write('\r'+'loading '+char)
#             time.sleep(.1)
#             sys.stdout.flush()



def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    print(path)
    return path


def upload_IGES_file(event=None):
    print("iges")
    path_iges = get_path("IGES files (*.iges)|*.iges|IGS files (*.igs)|*.igs")
    if path_iges ==  None:
        print("none file")
        return
    else:
        shapes = read_iges_file(path_iges)
        display.EraseAll()
        display.DisplayShape(shapes, update=True)


def Upload_STEP_file(event=None):
    print("step")
    path_step = get_path("STEP files (*.step)|*.step|STP files (*.stp)|*.stp")
  
    if path_step ==  None:
        print("none file")
        return
    else:
        shapes = read_step_file(path_step)
        display.EraseAll()
        display.DisplayShape(shapes, update=True)


def upload_IGES_bigFile(event=None):
    print("big iges file")
    path_iges = get_path("IGES files (*.iges)|*.iges|IGS files (*.igs)|*.igs")
    if path_iges ==  None:
        print("none file")
        return
    else:
        shapes = read_iges_file(path_iges)
        display.EraseAll()
        # render in x3dom
        my_renderer = x3dom_renderer.X3DomRenderer()
        my_renderer.DisplayShape(shapes)
        my_renderer.render(open_webbrowser=True)

def upload_STEP_bigFile(event=None):
    print("big step file")
    path_step = get_path("STEP files (*.step)|*.step|STP files (*.stp)|*.stp")
    if path_step ==  None:
        print("none file")
        return
    else:
        shape = read_step_file(path_step)
        display.EraseAll()
        # render in x3dom
        my_renderer = x3dom_renderer.X3DomRenderer()
        my_renderer.DisplayShape(shape)
        my_renderer.render( open_webbrowser=True)

        
def exit(event=None):
    sys.exit()


if __name__ == '__main__':
    # display, start_display, add_menu, add_function_to_menu = init_display("qt-pyqt5")
    display, start_display, add_menu, add_function_to_menu = init_display("wx")
    add_menu('File')
    add_function_to_menu('File', upload_IGES_file )
    add_function_to_menu('File', Upload_STEP_file )
    add_function_to_menu('File', upload_IGES_bigFile)
    add_function_to_menu('File', upload_STEP_bigFile)
    add_function_to_menu('File', exit )
    start_display()
