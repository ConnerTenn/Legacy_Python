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
        self.ObjectList = []
        self.Disp = False

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
            #print("ObjectList: %s" % (self.ObjectList))
            print()
            for x in self.ObjectList:
                if x == self.Ball1:
                    print('Ball1')
                if x == self.Ball2:
                    print('Ball2')
                if x == self.Ball3:
                    print('Ball3')

################################################################################

    def End(self):
        self.Play=False
        
    def StartUp(self):
        self.Ball1 = Objects(1, 0, 1)
        self.ObjectList.append(self.Ball1)
        self.Ball2 = Objects(1, 0, 30)
        self.ObjectList.append(self.Ball2)
        self.Ball3 = Objects(0, 0, 5)
        self.ObjectList.append(self.Ball3)
        self.camera = Camera()
        Main.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.canvas.delete(ALL)
            self.EventCheck()
            self.camera.Draw()
            self.Disp = False
            self.Ball2.PosZ = self.Ball2.PosZ + 0.01
            
            self.canvas.update()
            play = False
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
        Main.camera.GetOrder()
        Main.camera.DefObjectProjection()
        Main.camera.DefSizeProjection()
        Main.camera.DrawObjects()

    def GetOrder(self):
        Count= -1
        Count2= -1
        NewList = []
        NewListConfig = []
        for Object in Main.ObjectList:
            Count = Count + 1

            if (NewList == []):
                NewList.append(Object)
            else:
                for Object2 in NewList:
                    print(Count2)
                    Count2 = Count2 + 1
                    if self.GreaterDistance(Object, Object2):
                        NewListConfig = self.AddBetween(NewListConfig, Count2+1, Object)
                    else:
                        NewListConfig = self.AddBetween(NewListConfig, Count2, Object)
                NewList = NewListConfig
                '''for x in NewList:
                    if x == Main.Ball1:
                        print('Ball1')
                    if x == Main.Ball2:
                        print('Ball2')
                    if x == Main.Ball3:
                        print('Ball3')'''
        Main.ObjectList = NewList
                    
    def AddBetween(self, List, Pos, Item):
        PrevList = []
        AfterList = []
        NewList = []
        for x in range(0, Pos):
            PrevList.append(List[x])
        for x in range(Pos, len(List)):
            AfterList.append(List[x])
        NewList = NewList + (PrevList)
        NewList = NewList + [Item]
        NewList = NewList + (AfterList)
        return(NewList)

    def GreaterDistance(self, Object1, Object2):
        if sqrt(pow(Object1.PosX, 2) + pow(Main.camera.PosX, 2)) > sqrt(pow(Object2.PosX, 2) + pow(Main.camera.PosX, 2)):
            return True
        else:
            return False
        
            
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
            Main.canvas.create_oval(Object.ProjectX - Object.ProjectSize/2, 100 - Object.ProjectSize/2, Object.ProjectX + Object.ProjectSize/2, 100 + Object.ProjectSize/2 , fill ='blue')

#Start
Main=Main(Title = "2D Projections V1.0", Height=200, Width=200);
Main.StartUp();
