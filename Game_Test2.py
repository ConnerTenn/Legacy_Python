#Imports
import time
from tkinter import *

#Start
Height=200
Width=300
tk=Tk()
canvas=Canvas(tk, height=Height, width=Width)
canvas.pack()

#Functions
def Event(event):
    if event.keysym=='Escape':
        End()
    Update(event.keysym, Extract(event))

def Extract(Char_Code):
    Copy=(str(Char_Code))
    Text=Copy[25:35]
    return Text
    
def End():
    Clear()
    canvas.create_text(Width/2, Height/2, text='Shutting Down...', font=('times', 20), fill='red')
    canvas.update()
    time.sleep(1)
    exit(0)

def Clear():
    canvas.create_rectangle(-Width, -Height, Width*2, Height*2, outline='white', fill='white')

def Update(Event,Char_Code):
    Clear()
    canvas.create_text(Width/2, Height/2, text=('%s (%s)' % (Event, Char_Code)), font=('times', 15), fill='blue')

#Main
Update('Type', 'Escape to close')

canvas.bind_all('<KeyPress->', Event)


