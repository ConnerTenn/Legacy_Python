#Imports
from tkinter import *
import time

#Classes
class Main:
    def __init__(self, Width=500, Height=400, Title="Python Program"):
        self.Width=Width
        self.Height=Height
        self.Title=Title

        self.Right=0
        self.Up=0
        self.Play=True
        self.tk=Tk()
        self.tk.title(self.Title)
        self.tk.resizable(0,0)
        self.canvas=Canvas(self.tk, width=self.Width, height=self.Height)
        self.canvas.pack()

        self.KeyBindings=['q','w','s','a','d']
        self.Pressed={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=False
            self.tk.bind("<KeyPress-%s>" % Event, self.KeyPressed)
            self.tk.bind("<KeyRelease-%s>" % Event, self.KeyReleased)
        
    def End(self):
        self.Play=False
        
    def StartUp(self):
        self.Box=self.canvas.create_rectangle(5,5,20,20,fill='red')
        Main.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            Main.EventCheck()
            self.Move()
            self.Right=0
            self.Up=0
            time.sleep(0.01)
            self.canvas.update()
        exit(0)
        
    def KeyPressed(self, event):
        self.Pressed[event.char]=True
        
    def KeyReleased(self, event):
        self.Pressed[event.char]=False

    def EventCheck(self):
        if self.Pressed['q']==True:
            Main.End()
        if self.Pressed['w']==True:
            self.Up=-1
        if self.Pressed['s']==True:
            self.Up=1
        if self.Pressed['a']==True:
            self.Right=-1
        if self.Pressed['d']==True:
            self.Right=1

    def Move(self):
        self.canvas.move(self.Box, self.Right, self.Up)

#Start
Main=Main(Title='Key Events')
Main.StartUp()








