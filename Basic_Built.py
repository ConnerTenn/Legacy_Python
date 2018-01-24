#Imports
from tkinter import *

#Classes
class Main:
    def __init__(self, Width=500, Height=400, Title="Python Program"):
        self.Width=Width
        self.Height=Height
        self.Title=Title

        self.tk=Tk()
        self.tk.title(self.Title)
        self.tk.resizable(0,0)
        self.canvas=Canvas(self.tk, width=self.Width, height=self.Height)
        self.canvas.pack()
            
    def Startup():
        Main.MainLoop()

    def Mainloop():
        pass

    def Event(event):
        print('w')
        

#Start
Main=Main()
Main.Startup
