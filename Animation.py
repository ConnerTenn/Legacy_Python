# Imports
import time
from tkinter import *

#Variables
Height=600
Width=1000
x1=10
y1=10
x2=60
y2=20
colour='red'

#Functions
def move(event):
    if event.keysym=='Up':
        canvas.move(1,0,-3)
    elif event.keysym=='Down':
        canvas.move(1,0,3)
    elif event.keysym=='Left':
        canvas.move(1,-3,0)
    elif event.keysym=='Right':
        canvas.move(1,3,0)

#Main
tk=Tk()
canvas=Canvas(tk, height=Height, width=Width)
canvas.pack()
canvas.create_rectangle(x1,x2,x2,y2, fill=colour)

canvas.bind_all('<KeyPress-Up>',move)
canvas.bind_all('<KeyPress-Down>',move)
canvas.bind_all('<KeyPress-Left>',move)
canvas.bind_all('<KeyPress-Right>',move)
canvas.bind_all('<KeyPress-Return>',move)
exit
