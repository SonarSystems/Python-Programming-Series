#!/usr/bin/python3

import tkinter
from tkinter import *

window = tkinter.Tk()

stringVar = StringVar()
lbl = Label(window, textvariable = stringVar )

stringVar.set("Awesome label text")
lbl.pack()

window.mainloop()
