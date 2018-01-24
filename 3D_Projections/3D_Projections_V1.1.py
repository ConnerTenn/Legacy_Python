#Imports
from tkinter import *
from math import *

#Classes

############################################################################
class Main:
    def __init__(self, Width=500, Height=400, Title="Python Program"):
        self.Width=Width
        self.Height=Height
        self.Title=Title

        self.Play=True
        self.ObjectList = [];

        self.tk=Tk()
        self.tk.title(self.Title)
        self.tk.resizable(0,0)
        self.canvas=Canvas(self.tk, width=self.Width, height=self.Height)
        self.canvas.pack()

#---------------------------------------------------------------------------

        self.KeyBindings=['q', 'r']
        self.Pressed={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=False
            self.tk.bind("<KeyPress-%s>" % Event, self.KeyPressed)
            self.tk.bind("<KeyRelease-%s>" % Event, self.KeyReleased)

    def KeyPressed(self, event):
        self.Pressed[event.char]=True
        
    def KeyReleased(self, event):
        self.Pressed[event.char]=False

    def EventCheck(self):
        if self.Pressed['q']==True:
            Main.End()
        if self.Pressed['r']==True:
            print("Ball.ProjectX: %s, Ball.PosX: %s, Ball.PosZ: %s" % (self.Ball1.ProjectX, self.Ball1.PosX, self.Ball1.PosZ))

################################################################################

    def End(self):
        self.Play=False
        
    def StartUp(self):
        self.Ball1 = Objects(1, 0, 1)
        self.ObjectList.append(self.Ball1)
        self.Ball2 = Objects(1, 0, 30)
        self.ObjectList.append(self.Ball2)
        self.Ball3 = Objects(0, 0, 1)
        self.ObjectList.append(self.Ball3)
        self.camera = Camera()
        Main.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.EventCheck()
            self.camera.Draw()
            
            self.canvas.update()
        exit(0);

################################################################################
################################################################################
class Objects:
    def __init__(self, PosX, PosY, PosZ, Size=1):
        self.PosX = PosX
        self.PosY = PosY
        self.PosZ = PosZ
        self.ProjectX = 0
        self.ProjectY = 0
        self.Size = Size
        self.ProjectSize = Size

################################################################################
################################################################################
class Camera:
    def __init__(self):
        '''3D Vars'''
        self.PosX = 0
        self.PosY = 0
        self.PosZ = 0
        self.RotationX = 0
        self.RotationY = 90
        self.RotationZ = 0
        '''2D Vars'''
        self.ViewAngleX = 45
        self.ViewAngleY = 45
        self.ViewSizeX = 200
        self.ViewSizeY = 200
        self.FOVX = 200
        self.FOVY = 200
        
    def Draw(self):
        Main.camera.DefObjectProjection()
        Main.camera.DefSizeProjection()
        Main.camera.DrawObjects()

    def DefObjectProjection(self):
        for Object in Main.ObjectList:
            Xoff = Object.PosX - Main.camera.PosX
            Zoff = Object.PosZ - Main.camera.PosZ
            #print("Xoff: %s, Zoff: %s, Sqrt: %s" % (Xoff, Zoff, math.sqrt((Xoff^2) + (Zoff^2))))
            AngleX = round(degrees(asin(Xoff/sqrt(pow(Xoff,2) + pow(Zoff,2)))), 1)
            Object.ProjectX = self.ViewSizeX/2 + ((AngleX/self.ViewAngleX) * (self.ViewSizeX/2))

    def DefSizeProjection(self):
        for Object in Main.ObjectList:
            Distance = abs(Object.PosZ - Main.camera.PosZ)
            Object.ProjectSize = Main.camera.ViewAngleX - Distance * Object.Size
            #print(Object.ProjectSize)
            
    def DrawObjects(self):
        for Object in Main.ObjectList:
            if(Object == Main.Ball1):
                Main.canvas.create_oval(Object.ProjectX - Object.ProjectSize/2, 100 - Object.ProjectSize/2, Object.ProjectX + Object.ProjectSize/2, 100 + Object.ProjectSize/2 , fill='blue')
            else:
                Main.canvas.create_oval(Object.ProjectX - Object.ProjectSize/2, 100 - Object.ProjectSize/2, Object.ProjectX + Object.ProjectSize/2, 100 + Object.ProjectSize/2 )

#Start
Main=Main(Title = "2D Projections V1.0", Height=200, Width=200);
Main.StartUp();
