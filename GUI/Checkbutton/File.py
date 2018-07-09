#!/usr/bin/python3

import tkinter
from tkinter import *

window = tkinter.Tk()

cv = IntVar()
cb = Checkbutton(window, text = "Text", variable = cv, onvalue = 1, offvalue = 0, height=5, width = 20, )
cb.pack()

window.mainloop()
