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
        self.ButtonList1=[]
        self.ButtonList2=[]
        self.PlayerList=[]
        self.WallList=[]
        self.TriggerWallList=[]
        self.ThruWallList=[]
        
        self.tk=Tk()
        self.tk.title(self.Title)
        self.tk.resizable(0,0)
        self.canvas=Canvas(self.tk, width=self.Width, height=self.Height)
        self.canvas.pack()

#---------------------------------------------------------------------------

        self.KeyBindings=['q', ' ', 'w', 's', 'a', 'd', 'i', 'j', 'l']
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
                self.Level1StartUp()
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

################################################################################
    def CheckEnd(self):
        if self.player1.WithinX(self.player1.Coords, self.EndLocation) and self.player1.WithinY(self.player1.Coords, self.EndLocation) \
           and self.player2.WithinX(self.player2.Coords, self.EndLocation) and self.player2.WithinY(self.player2.Coords, self.EndLocation):
            if self.GameProgress=='Level1Loop':
                self.Level1ShutDown()
        
    def End(self):
        self.Play=False
        exit(0)
        
    def MainStartUp(self):
        self.GameProgress='START'
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Start_Screen.gif")
        self.StartImage=self.canvas.create_image(0, 0, anchor=NW, image=self.StartImageFile)
        while 1:
            self.EventCheck()
            self.canvas.update()

    def Level1StartUp(self):
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
        
        self.wall1=Wall(0,593, 899, 599)#Botoom Side
        self.ObjectList.append(self.wall1)
        self.WallList.append(self.wall1)

        self.wall2=Wall(0,0, 7, 599)#Left Side
        self.ObjectList.append(self.wall2)
        self.WallList.append(self.wall2)

        self.wall3=Wall(0,0, 899, 5)#Top Side
        self.ObjectList.append(self.wall3)
        self.WallList.append(self.wall3)

        self.wall4=Wall(893,0, 899, 599)#Right Side
        self.ObjectList.append(self.wall4)
        self.WallList.append(self.wall4)

        self.wall5=Wall(650, 500, 800, 510)
        self.ObjectList.append(self.wall5)
        self.WallList.append(self.wall5)

        self.thruwall1=ThruWall(650, 500, 660, 600-6)
        self.ThruWallList.append(self.thruwall1)
        
        self.triggerwall1=TriggerWall(700, 6, 710, 600-6, True)
        self.ObjectList.append(self.triggerwall1)
        self.TriggerWallList.append(self.triggerwall1)
        self.triggerwall1remove=True

        self.triggerwall2=TriggerWall(670, 6, 680, 600-6, True)
        self.ObjectList.append(self.triggerwall2)
        self.TriggerWallList.append(self.triggerwall2)
        self.triggerwall2remove=True

        self.button1p1=Button(260, 430, 'triggerwall1', 1)
        self.ButtonList1.append(self.button1p1)

        self.button1p2=Button(280, 430, 'triggerwall2', 2)
        self.ButtonList2.append(self.button1p2)

        self.EndLocation=[900-60, 0, 900, 600]
        EndImage=self.canvas.create_rectangle(900-80, 7, 900-6, 600-4, outline="red", stipple="gray50", width=4)

        self.Level1Loop()
        
    def Level1Loop(self):
        while self.Play==True:
            self.EventCheck()
            self.player1.Fall()
            self.player2.Fall()
            self.CheckEnd()
            
            Button.ButtonCheck()
                        
            self.canvas.update()
            time.sleep(0.01)
        exit(0)

    def Level1ShutDown(self):
        self.ButtonList=[]
        self.ObjectList=[]
        self.WallList=[]
        self.PlayerList=[]
        self.Level1StartUp()
        
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
        if self==Main.player2:
            for Object in Main.ThruWallList:
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
        if self==Main.player2:
            for Object in Main.ThruWallList:
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
        if self==Main.player2:
            for Object in Main.ThruWallList:
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
        if self==Main.player2:
            for Object in Main.ThruWallList:
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
    def __init__(self, PosX, PosY, PosX2, PosY2):
        self.PosX=PosX
        self.PosY=PosY
        self.PosX2=PosX2
        self.PosY2=PosY2
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX2
        self.CoordsY2=self.PosY2
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        #self.ImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Player1.gif")
        #self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile)
        self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, fill='black')

################################################################################
################################################################################
class ThruWall(Objects):
    def __init__(self, PosX, PosY, PosX2, PosY2):
        self.PosX=PosX
        self.PosY=PosY
        self.PosX2=PosX2
        self.PosY2=PosY2
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX2
        self.CoordsY2=self.PosY2
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        #self.ImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Player1.gif")
        #self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile)
        self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, fill='gray')
        
################################################################################
################################################################################
class TriggerWall(Objects):
    def __init__(self, PosX, PosY, PosX2, PosY2, InitialState=True):
        self.PosX=PosX
        self.PosY=PosY
        self.PosX2=PosX2
        self.PosY2=PosY2
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX2
        self.CoordsY2=self.PosY2
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        #self.ImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Player1.gif")
        #self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile)
        if InitialState:
            self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, outline='lightgreen', fill='lightgreen')
        else: 
            self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, outline='lightgreen', stripple='gray50', width=3)
################################################################################
################################################################################  
class Button(Objects):
    def __init__(self, PosX, PosY, Action, Player):
        self.Action=Action
        self.PosX=PosX
        self.PosY=PosY
        self.PosX2=PosX+20
        self.PosY2=PosY+15
        self.CoordsX1=self.PosX
        self.CoordsY1=self.PosY
        self.CoordsX2=self.PosX2
        self.CoordsY2=self.PosY2
        self.Coords=[self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2]
        self.ImageFile=[PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\ButtonUnpressed1.gif"), \
                        PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\ButtonPressed1.gif"), \
                        PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\ButtonUnpressed2.gif"), \
                        PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\ButtonPressed2.gif")]
        if Player==1:
            self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile[0])
        elif Player==2:
            self.Image=Main.canvas.create_image(self.PosX, self.PosY, anchor=NW, image=self.ImageFile[2])
        #self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, fill='red')

    def ButtonCheck():
        if Main.GameProgress=='Level1Loop':
            if Main.player1.ButtonCheck()=='triggerwall1' and Main.triggerwall1remove:
                Main.ObjectList.remove(Main.triggerwall1)
                Main.TriggerWallList.remove(Main.triggerwall1)
                Main.triggerwall1remove=False
                Main.canvas.delete(Main.triggerwall1.Image)
                Main.canvas.itemconfig(Main.triggerwall1.Image, image=Main.canvas.create_rectangle(Main.triggerwall1.CoordsX1, Main.triggerwall1.CoordsY1, Main.triggerwall1.CoordsX2, Main.triggerwall1.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
            if Main.player1.ButtonCheck()=='triggerwall1': 
                Main.canvas.itemconfig(Main.button1p1.Image, image=Main.button1p1.ImageFile[1])
            else:
                Main.canvas.itemconfig(Main.button1p1.Image, image=Main.button1p1.ImageFile[0])
#-------------------------------------------------------------------------------------------------------------
            if Main.player2.ButtonCheck()=='triggerwall2' and Main.triggerwall2remove:
                Main.ObjectList.remove(Main.triggerwall2)
                Main.TriggerWallList.remove(Main.triggerwall2)
                Main.triggerwall2remove=False
                Main.canvas.delete(Main.triggerwall2.Image)
                Main.canvas.itemconfig(Main.triggerwall2.Image, image=Main.canvas.create_rectangle(Main.triggerwall2.CoordsX1, Main.triggerwall2.CoordsY1, Main.triggerwall2.CoordsX2, Main.triggerwall2.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
            if Main.player2.ButtonCheck()=='triggerwall2': 
                Main.canvas.itemconfig(Main.button1p2.Image, image=Main.button1p2.ImageFile[3])
            else:
                Main.canvas.itemconfig(Main.button1p2.Image, image=Main.button1p2.ImageFile[2])


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

    def ButtonCheck(self):
        for Buttons in Main.ButtonList1:
            if self.WithinY(self.Coords, Buttons.Coords) and self.WithinX(self.Coords, Buttons.Coords):
                return Buttons.Action

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

    def ButtonCheck(self):
        for Buttons in Main.ButtonList2:
            if self.WithinY(self.Coords, Buttons.Coords) and self.WithinX(self.Coords, Buttons.Coords):
                return Buttons.Action

################################################################################
################################################################################

class platform(Objects):
    pass

#Start
Main=Main(Width=900, Height=600, Title='Platformer V1.2.0')
Main.MainStartUp()
