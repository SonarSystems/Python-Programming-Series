#!/usr/bin/python3

import tkinter
from tkinter import *

window = tkinter.Tk()

string = StringVar()
lbl = Message(window, textvariable = string)

string.set("The most epic piece of string ever!")
lbl.pack()

window.mainloop()
