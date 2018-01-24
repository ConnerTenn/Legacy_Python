#Imports
from tkinter import *
import time
from math import *

#Variables
Play=1
Width=600
Height=600
CurrentImage=0
Angle=0
Speed=0.1
Offset=5
Delay=0.05
StartX=80
StartY=80

#Setup
tk=Tk()
canvas=Canvas(tk, width=Width, height=Height)
canvas.pack()

#Classes
class Box():
    def __init__(self):
        self.images=[
            PhotoImage(file='C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Animate_Box\\Figure-1.gif'),
            PhotoImage(file='C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Animate_Box\\Figure-2.gif'),
            PhotoImage(file='C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Animate_Box\\Figure-3.gif')
            ]
    
#Main
box=Box()
boximage=canvas.create_image(StartX,StartY,anchor=NW, image=box.images[CurrentImage])
canvas.update()
while Play:
    if CurrentImage>=2:
        CurrentImage=0
    else:
        CurrentImage=CurrentImage+1
        
    Angle=Angle+Speed
    Up=sin(Angle)*Offset
    Right=cos(Angle)*Offset

    canvas.itemconfig(boximage,image=box.images[CurrentImage])
    canvas.move(boximage, Right, Up)

    canvas.update()
    time.sleep(Delay)





    
