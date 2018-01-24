#Imports
from tkinter import *
import time
import sys

#Variables
Width=500
Height=600
Speed=5
Delay=0.04
Length=500

#Start
tk=Tk()
canvas=Canvas(tk, width=Width, height=Height)
canvas.pack()

#Functions
def End(event):
    print("Closing...")
    sys.exit()
    exit
    quit()
    raise SystemExit
    tk.exit()
    
#Classes
class Player:
    def __init__(self,Player_Number, Pos_X, Pos_Y, Colour):
        self.Player_Number=Player_Number
        self.Pos_X=Pos_X
        self.Pos_Y=Pos_Y
        self.Colour=Colour
        self.Up_Direction=1
        self.Right_Direction=1

#Main
Player_1=Player(1,10,10,'red')
Player_1_Rect=canvas.create_rectangle(Player_1.Pos_X-5, Player_1.Pos_Y+5, Player_1.Pos_X+5, Player_1.Pos_Y-5, fill=Player_1.Colour)

canvas.bind_all('<KeyPress-Return>', End)

while True:
    canvas.move(Player_1_Rect, Speed*Player_1.Right_Direction, Speed*Player_1.Up_Direction)
    
    Player_1.Pos_X=Player_1.Pos_X+Speed*Player_1.Right_Direction
    Player_1.Pos_Y=Player_1.Pos_Y+Speed*Player_1.Up_Direction

    if Player_1.Pos_X>Width-5 or Player_1.Pos_X<5:
        Player_1.Right_Direction=-(Player_1.Right_Direction)
    if Player_1.Pos_Y>Height-5 or Player_1.Pos_Y<5:
        Player_1.Up_Direction=-(Player_1.Up_Direction)
        
    canvas.update()
    time.sleep(Delay)


