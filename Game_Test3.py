#Imports
from tkinter import *
import time

#Variables
Height=200
Width=400
Play=1
Delay=0.01
Player_Height=40
Player_Width=5
Ball_Width=15
Ball_Height=15

#Start
tk=Tk()
canvas=Canvas(tk, height=Height, width=Width)
canvas.pack()

#Functions
def In_Event(event):
    if event.keysym=='Escape':
        global Play
        Play=0
    if event.keysym=='r':
        canvas.scale(Object_List['ball'], Width/2+Ball_Width/2, Height/2+Ball_Height/2, 1.04, 1.04)

def In_Event_P1(eventP1):
    if eventP1.keysym=='w':
        Player1.Move(0, -2)
    if eventP1.keysym=='s':
        Player1.Move(0, 2)
        
def In_Event_P2(eventP2):
    if eventP2.keysym=='o':
        Player2.Move(0, -2)
    if eventP2.keysym=='l':
        Player2.Move(0, 2)
        
#Classes
class Objects():
    def Move(self, x, y):
        self.canvas.move(self.id, x, y)
        self.x=self.x+x
        self.y=self.y+y

    def Draw(self):
        self.canvas.move(self.id, 0, 0)

class Ball(Objects):
    def __init__(self, canvas, X, Y, Vx, Vy, Colour):
        self.canvas=canvas
        self.id=canvas.create_oval(X, Y, X+Ball_Width, Y+Ball_Height, fill=Colour)
        self.x=X
        self.y=Y
        self.Vx=Vx
        self.Vy=Vy

class Players(Objects):
    def __init__(self, canvas, X, Y, Vx, Vy, Player_Width, Player_Height, Colour):
        self.canvas=canvas
        self.id=canvas.create_rectangle(X, Y, X+Player_Width, Y+Player_Height, fill=Colour)
        self.x=X
        self.y=Y
        self.Vx=Vx
        self.Vy=Vy
        
#Main
ball=Ball(canvas, Width/2, Height/2, 0, 0, 'blue')
Player1=Players(canvas, 10, Height/2-Player_Height/2, 0, 0, Player_Width, Player_Height, 'red')
Player2=Players(canvas, Width-10, Height/2-Player_Height/2, 0, 0, Player_Width, Player_Height, 'red')
Object_List={'ball':1, 'Player1':2, 'Player2':3}

canvas.bind_all('<KeyPress-Escape>', In_Event)
canvas.bind_all('<KeyPress-r>', In_Event)

canvas.bind_all('<KeyPress-w>', In_Event_P1)
canvas.bind_all('<KeyPress-s>', In_Event_P1)

canvas.bind_all('<KeyPress-o>', In_Event_P2)
canvas.bind_all('<KeyPress-l>', In_Event_P2)

while Play:
    ball.Move(ball.Vx, ball.Vy)
    Player1.Draw()
    tk.update()
    time.sleep(Delay)






print('Shutting Down...')








exit(0)
