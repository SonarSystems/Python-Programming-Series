#!/usr/bin/python3

import tkinter
from tkinter import *

window = tkinter.Tk()

lbl = Label(window, text = "Email")
lbl.pack(side = LEFT)
entr = Entry(window, bd = 3)
entr.pack(side = RIGHT)

window.mainloop()
