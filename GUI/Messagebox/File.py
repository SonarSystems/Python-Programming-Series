#!/usr/bin/python3

import tkinter
from tkinter import *

from tkinter import messagebox

window = Tk()

def func():
   messagebox.showinfo("Title", "Message")

btn = Button(window, text = "Click ME NOW", command = func)
btn.place(x = 0, y = 0)

window.mainloop()
