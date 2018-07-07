#!/usr/bin/python3

import tkinter
from tkinter import messagebox

window = tkinter.Tk()

canvasWidget = tkinter.Canvas(window, bg = "red", height = 512, width = 512)

coord = 10, 50, 512, 512
arcObject = canvasWidget.create_arc(coord, start = 0, extent = 270, fill = "white")
lineObject = canvasWidget.create_line(75, 10, 20, 150, fill = 'black')
canvasWidget.pack()

window.mainloop()
