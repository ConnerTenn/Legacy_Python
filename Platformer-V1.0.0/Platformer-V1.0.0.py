#Imports
from tkinter import *
import time

#Classes

############################################################################
class Main:
    def __init__(self, Width=500, Height=400, Title="Python Program"):
        self.Width=Width
        self.Height=Height
        self.Title=Title

        self.Play=True
        self.ObjectList=[]
        self.PlayerList=[]
        self.WallList=[]

        self.tk=Tk()
        self.tk.title(self.Title)
        self.tk.resizable(0,0)
        self.canvas=Canvas(self.tk, width=self.Width, height=self.Height)
        self.canvas.pack()

#---------------------------------------------------------------------------

        self.KeyBindings=['q', ' ', 'w', 's', 'a', 'd', 'i', 'j', 'l', 'p']
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
        if self.GameProgress=='START':
            if self.Pressed[' ']==True:
                self.Level1Startup()
        if self.GameProgress=='Level1Loop':
            if self.Pressed['w']:
                self.player1.FallSpeed=0.04
                self.player1.Jump()
            else:
                self.player1.FallSpeed=0.1
            if self.Pressed['a']:
                self.player1.VelosityX=-2
                self.player1.MoveHorisontal()
            if self.Pressed['d']:
                self.player1.VelosityX=2
                self.player1.MoveHorisontal()
                
            if self.Pressed['i']:
                self.player2.FallSpeed=0.03
                self.player2.Jump()
            else:
                self.player2.FallSpeed=0.08
            if self.Pressed['j']:
                self.player2.VelosityX=-2
                self.player2.MoveHorisontal()
            if self.Pressed['l']:
                self.player2.VelosityX=2
                self.player2.MoveHorisontal()

            if self.Pressed['p']:
                print(self.player1.Coords)
                print(self.player2.Coords)
                print()

################################################################################

    def End(self):
        self.Play=False
        
    def MainStartUp(self):
        self.GameProgress='START'
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Start_Screen.gif")
        self.StartImage=self.canvas.create_image(0, 0, anchor=NW, image=self.StartImageFile)
        while 1:
            self.EventCheck()
            self.canvas.update()

    def Level1Startup(self):
        self.GameProgress='Level1Loop'
        self.canvas.delete(self.StartImage)
        self.PlayImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\PlayBackground.gif")
        self.canvas.create_image(0, 0, anchor=NW, image=self.PlayImageFile)
        self.canvas.update()

        self.player1=Player1()
        self.ObjectList.append(self.player1)
        self.PlayerList.append(self.player1)

        self.player2=Player2()
        self.ObjectList.append(self.player2)
        self.PlayerList.append(self.player2)
        
        self.wall1=Wall(0,595, 899, 5)
        self.ObjectList.append(self.wall1)
        self.PlayerList.append(self.wall1)

        self.wall2=Wall(0,0, 7, 599)
        self.ObjectList.append(self.wall2)
        self.PlayerList.append(self.wall2)

        self.wall3=Wall(0,0, 899, 5)
        self.ObjectList.append(self.wall3)
        self.PlayerList.append(self.wall3)

        self.wall4=Wall(893,0, 7, 599)
        self.ObjectList.append(self.wall4)
        self.PlayerList.append(self.wall4)

        self.wall5=Wall(200,550, 400, 50)
        self.ObjectList.append(self.wall5)
        self.PlayerList.append(self.wall5)

        self.wall6=Wall(250,500, 400, 100)
        self.ObjectList.append(self.wall6)
        self.PlayerList.append(self.wall6)

        self.wall7=Wall(400,400, 5, 100)
        self.ObjectList.append(self.wall7)
        self.PlayerList.append(self.wall7)
        
        self.Level1Loop()
        
    def Level1Loop(self):
        while self.Play==True:
            self.EventCheck()
            self.player1.Fall()
            self.player2.Fall()
            self.canvas.update()
            time.sleep(0.01)
        exit(0)

################################################################################
################################################################################
class Objects:
    def WithinX(self, Cords1, Cords2):
        co1x1=Cords1[0]
        co1x2=Cords1[2]

        co2x1=Cords2[0]
        co2x2=Cords2[2]

        if ((co1x1 >= co2x1) and (co1x1 <= co2x2)) \
           or ((co1x2 >= co2x1) and (co1x2 <= co2x2)) \
           or ((co2x1 >= co1x1) and (co2x1 <= co1x2)) \
           or ((co2x2 >= co1x1) and (co2x2 <= co1x2)):
            return True
        else:
            return False

    def WithinY(self, Cords1, Cords2):
        co1y1=Cords1[1]
        co1y2=Cords1[3]

        co2y1=Cords2[1]
        co2y2=Cords2[3]

        if ((co1y1 > co2y1) and (co1y1 < co2y2)) \
           or ((co1y2 > co2y1) and (co1y2 < co2y2)) \
           or ((co2y1 > co1y1) and (co2y1 < co1y2)) \
           or ((co2y2 > co1y1) and (co2y2 < co1y2)):
            return True
        else:
            return False

    def CollideRight(self, Cords1, Cords2):
        co1x1=Cords1[0]-2
        co1x2=Cords1[2]
        co2x1=Cords2[0]
        co2x2=Cords2[2]
        if self.WithinY(Cords1, Cords2):
            if co1x1 <= co2x2 and co1x1 >=co2x1:
                return True
        return False
        
    def CollideLeft(self, Cords1, Cords2):
        co1x1=Cords1[0]
        co1x2=Cords1[2]+2
        co2x1=Cords2[0]
        co2x2=Cords2[2]
        if self.WithinY(Cords1, Cords2):
            if co1x2 >= co2x1 and co1x2 <=co2x2:
                return True
        return False
        
    def CollideBottom(self, Cords1, Cords2):
        co1y1=Cords1[1]-4
        co1y2=Cords1[3]
        co2y1=Cords2[1]
        co2y2=Cords2[3]
        if self.WithinX(Cords1, Cords2):
            if co1y1 <= co2y2 and co1y1 >=co2y1:
                return True
        return False
        
    def CollideTop(self, Cords1, Cords2):
        co1y1=Cords1[1]
        co1y2=Cords1[3]+4
        co2y1=Cords2[1]
        co2y2=Cords2[3]
        if self.WithinX(Cords1, Cords2):
            if co1y2 <= co2y2 and co1y2 >= co2y1:
                return True
        return False

    def OnGround(self):
        for Object in Main.ObjectList:
            if Object==self:
                pass
            else:
                if self.CollideTop(self.Coords, Object.Coords):
                    return True
        return False

    def HitTop(self):
        for Object in Main.ObjectList:
            if Object==self:
                pass
            else:
                if self.CollideBottom(self.Coords, Object.Coords):
                    return True
        return False

    def HitSideRight(self):
        for Object in Main.ObjectList:
            if Object==self:
                pass
            else:
                if self.CollideRight(self.Coords, Object.Coords):
                    return True
        return False

    def HitSideLeft(self):
        for Object in Main.ObjectList:
            if Object==self:
                pass
            else:
                if self.CollideLeft(self.Coords, Object.Coords):
                    return True
        return False
            
################################################################################
################################################################################
class Players(Objects):
    def Fall(self):
        if self.OnGround():
            self.Velosity=0
            '''if self.State=='Standing':
                Main.canvas.move(self.Image, 0, -0.5)
                self.PosY=self.PosY-0.5
                self.StateLift=True'''
            self.State='Standing'
        else:
            #if self.StateLift==False:
            self.State='Jumping/Falling'
            self.VelosityY=self.VelosityY+self.FallSpeed
            if self.VelosityY > 5:
                self.VelosityY=5
            self.MoveVertical()
            
        if self.HitTop():
            self.VelosityY=0.5
        self.UpdateCoords()

    def Jump(self):
        if self.State=='Standing':
            self.VelosityY=-2.5
            self.MoveVertical()

    def MoveVertical(self):
        Main.canvas.move(self.Image, 0, self.VelosityY)
        self.PosY=self.PosY+self.VelosityY
        self.UpdateCoords()

    '''def Walk(self):
        '''
 
    def MoveHorisontal(self):
        if (self.VelosityX > 0 and self.HitSideLeft()==False): #or (self.VelosityX > 0 and self.State=='Standing'):    
            Main.canvas.move(self.Image, self.VelosityX, 0)
            self.PosX=self.PosX+self.VelosityX
        elif (self.VelosityX < 0 and self.HitSideRight()==False): #or (self.VelosityX < 0 and self.State=='Standing'):
            Main.canvas.move(self.Image, self.VelosityX, 0)
            self.PosX=self.PosX+self.VelosityX
        else:
            self.VelosityX=0
        self.UpdateCoords()

    def UpdateCoords(self):
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX+self.Width
        self.CoordsY2=self.PosY+self.Height
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        
################################################################################
################################################################################
class Wall(Objects):
    def __init__(self, PosX, PosY, Width, Height):
        self.PosX=PosX
        self.PosY=PosY
        self.Width=Width
        self.Height=Height
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX+self.Width
        self.CoordsY2=self.PosY+self.Height
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        #self.ImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Player1.gif")
        #self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile)
        self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, fill='black')

################################################################################
################################################################################        
class Player1(Players):
    def __init__(self):
        self.VelosityY=0
        self.VelosityX=0
        self.FallSpeed=0
        self.State='Standing'
        self.StateLift=False
        self.PosX=20
        self.PosY=500
        self.Width=20
        self.Height=20
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX+self.Width
        self.CoordsY2=self.PosY+self.Height
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        self.ImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Player1.gif")
        self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile)
        #self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, fill='light green')

################################################################################
################################################################################        
class Player2(Players):
    def __init__(self):
        self.VelosityY=0
        self.VelosityX=0
        self.FallSpeed=0
        self.State='Standing'
        self.StateLift=False
        self.PosX=45
        self.PosY=500
        self.Width=15
        self.Height=30
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX+self.Width
        self.CoordsY2=self.PosY+self.Height
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        self.ImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Player2.gif")
        self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile)
        #self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, fill='light green')

################################################################################
################################################################################

class platform(Objects):
    pass

#Start
Main=Main(Width=900, Height=600, Title='Platformer V1.0.0')
Main.MainStartUp()
