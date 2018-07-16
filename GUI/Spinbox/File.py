#!/usr/bin/python3

import tkinter
from tkinter import *

window = Tk()

box = Spinbox(window, from_ = 0, to = 5)
box.pack()

window.mainloop()
