#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.17
# In conjunction with Tcl version 8.6
#    Dec 10, 2018 06:00:01 PM CET  platform: Windows NT

import sys
import subprocess

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    import Tkinter, Tkconstants, tkFileDialog
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    from tkinter import filedialog
    py3 = True

#Select root
def selectRoot():
    global gameRoot
    gameRoot = filedialog.askdirectory()
    w.dispResults.delete(0, END)
    w.dispResults.insert(0, gameRoot)

#Open the file selector and get the path to the file to be converted
def convert():
    global gameRoot
    if gameRoot == "":
        print("Debug1")
    Tk().withdraw()
    filename = filedialog.askopenfilename(initialdir = gameRoot ,title = "Select file",filetypes = (("xml files","*.xml"),("dae files","*.dae")))
    action = 'exportxmf'
    if filename.endswith('.xml'):
        action = 'importxmf'
    converter = "XRConvertersmain.exe"
    args = [action, gameRoot, filename]
    print(args)
    subprocess.call([converter, action, gameRoot, filename])

def init(top, gui, *args, **kwargs):
    global w, top_level, root, gameRoot
    w = gui
    top_level = top
    root = top
    gameRoot = ""

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


