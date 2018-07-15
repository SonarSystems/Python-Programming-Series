#!/usr/bin/python3

import tkinter
from tkinter import *

def getValue():
   selection = "Value = " + str(var.get())
   label.config(text = selection)

window = Tk()
var = DoubleVar()
scale = Scale(window, variable = var)
scale.pack()

button = Button(window, text = "Retrieve Value", command = getValue)
button.pack()

label = Label(window)
label.pack()

window.mainloop()
