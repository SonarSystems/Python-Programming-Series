#!/usr/bin/python3

import tkinter
from tkinter import messagebox

top = tkinter.Tk()

def PopupFunction():
   msg = messagebox.showinfo( "Popup Title", "Message")

buttonWidget = tkinter.Button(top, text = "Click Me", command = PopupFunction)
buttonWidget.place(x = 25,y = 100)

top.mainloop()
