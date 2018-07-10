#!/usr/bin/python3

import tkinter
from tkinter import *

window = tkinter.Tk()

lbox = Listbox(window)
lbox.insert(1, "Item 1")
lbox.insert(2, "Item 2")
lbox.insert(3, "Item 3")
lbox.insert(4, "Item 4")
lbox.insert(5, "Item 5")

lbox.pack()

window.mainloop()
