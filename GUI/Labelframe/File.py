#!/usr/bin/python3

import tkinter
from tkinter import *

window = Tk()

labelframe = LabelFrame(window, text = "This is a LabelFrame")
labelframe.pack(fill = "both", expand = "yes")
 
left = Label(labelframe, text = "Inside the LabelFrame")
left.pack()

window.mainloop()
