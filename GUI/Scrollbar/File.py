#!/usr/bin/python3

import tkinter
from tkinter import *

window = Tk()
scrollBar = Scrollbar(window)
scrollBar.pack(side = RIGHT, fill = Y)

myList = Listbox(window, yscrollcommand = scrollBar.set )
for line in range(1000):
   myList.insert(END, "Row " + str(line + 1))

myList.pack()
scrollBar.config(command = myList.yview)


window.mainloop()
