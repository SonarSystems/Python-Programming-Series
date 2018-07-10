#!/usr/bin/python3

import tkinter
from tkinter import *

def select():
   selection = "Awesome option " + str(var.get())
   label.config(text = selection)

window = Tk()

var = IntVar()
radio1 = Radiobutton(window, text = "Option 1", variable = var, value = 1, command = select)
radio1.pack( anchor = W )

radio2 = Radiobutton(window, text = "Option 2", variable = var, value = 2, command = select)
radio2.pack( anchor = W )

radio3 = Radiobutton(window, text = "Option 3", variable = var, value = 3, command = select)
radio3.pack( anchor = W)

radio4 = Radiobutton(window, text = "Option 4", variable = var, value = 4, command = select)
radio4.pack( anchor = W)

label = Label(window)
label.pack()

window.mainloop()
