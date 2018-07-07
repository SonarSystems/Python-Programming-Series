#!/usr/bin/python3

import tkinter
from tkinter import messagebox

window = tkinter.Tk()

def PopupFunction():
   msg = messagebox.showinfo( "Popup Title", "Message")

buttonWidget = tkinter.Button(window, text = "Click Me", command = PopupFunction)
buttonWidget.place(x = 25,y = 100)

window.mainloop()
