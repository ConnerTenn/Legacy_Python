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
        self.Released={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=False
            self.Released[Event]=True
            self.tk.bind("<KeyPress-%s>" % Event, self.KeyPressed)
            self.tk.bind("<KeyRelease-%s>" % Event, self.KeyReleased)

    def KeyPressed(self, event):
        self.Pressed[event.char]=True
        self.Released[event.char]=False
        
    def KeyReleased(self, event):
        self.Pressed[event.char]=False
        self.Released[event.char]=True

    def EventCheck(self):
        if self.Pressed['q']==True:
            Main.End()
        #-------    
        if self.GameProgress=='START':
            if self.Pressed[' ']==True:
                self.GameProgress='START2'
        #-------
        if self.GameProgress=='START2':
            if self.Released[' ']==True:
                self.Level4Start()
        #-------    
        if self.GameProgress=='Level1Start':
            if self.Pressed[' ']==True:
                self.Level1Startup()
        #-------
        if self.GameProgress=='Level2Start':
            if self.Pressed[' ']==True:
                self.Level2Startup()
        #-------
        if self.GameProgress=='Level3Start':
            if self.Pressed[' ']==True:
                self.Level3Startup()
        #-------
        if self.GameProgress=='Level4Start':
            if self.Pressed[' ']==True:
                self.Level4Startup()
        #-------
        if self.GameProgress=='Level1Loop' or self.GameProgress=='Level2Loop' or self.GameProgress=='Level3Loop' or self.GameProgress=='Level4Loop':
            if self.Pressed['w']:
                self.player1.FallSpeed=0.02
                self.player1.Jump()
            else:
                self.player1.FallSpeed=0.03
            if self.Pressed['a']:
                self.player1.VelosityX=-1
                self.player1.MoveHorisontal()
            if self.Pressed['d']:
                self.player1.VelosityX=1
                self.player1.MoveHorisontal()
                
            if self.Pressed['i']:
                self.player2.FallSpeed=0.02
                self.player2.Jump()
            else:
                self.player2.FallSpeed=0.03
            if self.Pressed['j']:
                self.player2.VelosityX=-1
                self.player2.MoveHorisontal()
            if self.Pressed['l']:
                self.player2.VelosityX=1
                self.player2.MoveHorisontal()

################################################################################
    def CheckEnd(self):
        if self.player1.WithinX(self.player1.Coords, self.EndLocation) and self.player1.WithinY(self.player1.Coords, self.EndLocation) \
           and self.player2.WithinX(self.player2.Coords, self.EndLocation) and self.player2.WithinY(self.player2.Coords, self.EndLocation):
            if self.GameProgress=='Level1Loop':
                self.Level1ShutDown()
            if self.GameProgress=='Level2Loop':
                self.Level2ShutDown()
            if self.GameProgress=='Level3Loop':
                self.Level3ShutDown()
            if self.GameProgress=='Level4Loop':
                self.Level4ShutDown()
        
    def End(self):
        self.Play=False
        exit(0)
        
    def MainStartup(self):
        self.GameProgress='START'
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Title_Screen.gif")
        self.StartImage=self.canvas.create_image(1, 1, anchor=NW, image=self.StartImageFile)
        self.canvas.update()
        while 1:
            self.EventCheck()
            self.canvas.update()
        self.Level1Start()

#==========================================================================================
    def Level1Start(self):
        self.GameProgress='Level1Start'
        self.canvas.delete(self.StartImage)
                    
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Start_Screen2.gif")
        self.Level1StartImage=self.canvas.create_image(0, 0, anchor=NW, image=self.StartImageFile)
        self.Level1StartText1=self.canvas.create_text(900/2, 600/2, fill='lightgreen', font=('times', 40), text='Level 1')
        self.Level1StartText2=self.canvas.create_text(900/2, 600/2+50, fill='lightgreen', font=('times', 40), text='Press Space to Continue')
        self.canvas.update()
        while 1:
            self.EventCheck()
            self.canvas.update()

    def Level1Startup(self):
            self.GameProgress='Level1Startup'
            self.canvas.delete(self.Level1StartImage)
            self.canvas.delete(self.Level1StartText1)
            self.canvas.delete(self.Level1StartText2)
            
            self.PlayImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\PlayBackground.gif")
            self.canvas.create_image(1, 1, anchor=NW, image=self.PlayImageFile)

            self.player1=Player1(45, 500)
            self.ObjectList.append(self.player1)
            self.PlayerList.append(self.player1)

            self.player2=Player2(70, 500)
            self.ObjectList.append(self.player2)
            self.PlayerList.append(self.player2)
            
            self.wall1=Wall(0,570, 899, 599)#Botoom Side
            self.ObjectList.append(self.wall1)
            self.WallList.append(self.wall1)

            self.wall2=Wall(0,0, 30, 599)#Left Side
            self.ObjectList.append(self.wall2)
            self.WallList.append(self.wall2)

            self.wall3=Wall(0,0, 899, 200)#Top Side
            self.ObjectList.append(self.wall3)
            self.WallList.append(self.wall3)

            self.wall4=Wall(893,0, 899, 599)#Right Side
            self.ObjectList.append(self.wall4)
            self.WallList.append(self.wall4)

            self.wall5=Wall(200,520, 600, 599)#Base Platform
            self.ObjectList.append(self.wall5)
            self.WallList.append(self.wall5)

            self.wall6=Wall(300,465, 600, 599)#Platform
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall7=Wall(0,0, 180, 430)#Drop-Down Left
            self.ObjectList.append(self.wall7)
            self.WallList.append(self.wall7)

            self.wall7=Wall(700,0, 899, 430)#Drop-Down Right
            self.ObjectList.append(self.wall7)
            self.WallList.append(self.wall7)

            self.EndLocation=[900-60, 430+3, 900, 600]
            EndImage=self.canvas.create_rectangle(900-85, 430+3, 900-9, 570-2, outline="red", stipple="gray50", width=4)
            
            self.Level1Loop()
        
    def Level1Loop(self):
        self.GameProgress='Level1Loop'
        while self.Play==True:
            self.EventCheck()
            self.player1.Fall()
            self.player2.Fall()
            self.CheckEnd()
                        
            self.canvas.update()
            time.sleep(0.005)
        exit(0)

    def Level1ShutDown(self):
        self.ObjectList=[]
        self.ButtonList1=[]
        self.ButtonList2=[]
        self.PlayerList=[]
        self.WallList=[]
        self.TriggerWallList=[]
        self.ThruWallList=[]
        self.Level2Start()
        
#==========================================================================================
    def Level2Start(self):
        self.GameProgress='Level2Start'
        self.canvas.delete(self.StartImage)
                    
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Start_Screen2.gif")
        self.Level2StartImage=self.canvas.create_image(0, 0, anchor=NW, image=self.StartImageFile)
        self.Level2StartText1=self.canvas.create_text(900/2, 600/2, fill='lightgreen', font=('times', 40), text='Level 2')
        self.Level2StartText2=self.canvas.create_text(900/2, 600/2+50, fill='lightgreen', font=('times', 40), text='Press Space to Continue')
        self.canvas.update()
        while 1:
            self.EventCheck()
            self.canvas.update()

    def Level2Startup(self):
            self.GameProgress='Level2Startup'
            self.canvas.delete(self.Level1StartImage)
            self.canvas.delete(self.Level1StartText1)
            self.canvas.delete(self.Level1StartText2)
            
            self.PlayImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\PlayBackground.gif")
            self.canvas.create_image(1, 1, anchor=NW, image=self.PlayImageFile)

            self.player1=Player1(45, 500)
            self.ObjectList.append(self.player1)
            self.PlayerList.append(self.player1)

            self.player2=Player2(70, 500)
            self.ObjectList.append(self.player2)
            self.PlayerList.append(self.player2)
            
            self.wall1=Wall(0,570, 899, 599)#Botoom Side
            self.ObjectList.append(self.wall1)
            self.WallList.append(self.wall1)

            self.wall2=Wall(0,0, 30, 599)#Left Side
            self.ObjectList.append(self.wall2)
            self.WallList.append(self.wall2)

            self.wall3=Wall(0,0, 899, 6)#Top Side
            self.ObjectList.append(self.wall3)
            self.WallList.append(self.wall3)

            self.wall4=Wall(893,0, 899, 599)#Right Side
            self.ObjectList.append(self.wall4)
            self.WallList.append(self.wall4)

            self.wall5=Wall(0,0, 195, 460)#Drop-Down Left
            self.ObjectList.append(self.wall5)
            self.WallList.append(self.wall5)

            self.wall6=Wall(0,460, 270, 470)#Drop-Down Left Extension Bottom
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall6=Wall(310, 510, 500, 600)#Middle Platform
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall6=Wall(310, 410, 500, 420)#Floating Platform Bottom
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall6=Wall(0,360, 270, 370)#Drop-Down Left Extension Bottom-Middle
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall6=Wall(310, 310, 500, 320)#Floating Platform Middle
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall6=Wall(0,260, 270, 270)#Drop-Down Left Extension Top-Middle
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall7=Wall(310, 210, 500, 220)#Floating Platform Middle
            self.ObjectList.append(self.wall7)
            self.WallList.append(self.wall7)

            self.wall6=Wall(0,160, 270, 170)#Drop-Down Left Extension Top
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall7=Wall(310, 110, 900, 120)#Floating Platform Top
            self.ObjectList.append(self.wall7)
            self.WallList.append(self.wall7)

            self.wall7=Wall(500, 120, 900, 600)#Floating Platform Top
            self.ObjectList.append(self.wall7)
            self.WallList.append(self.wall7)

            self.EndLocation=[900-60, 0+3, 900, 110]
            EndImage=self.canvas.create_rectangle(900-85, 7+3, 900-9, 110-2, outline="red", stipple="gray50", width=4)
            
            self.Level2Loop()
        
    def Level2Loop(self):
        self.GameProgress='Level2Loop'
        Time=0
        self.Level2Prompt1Bool=True
        while self.Play==True:
            Time=Time+0.005
            if Time>30 and self.Level2Prompt1Bool:
                self.Level2Prompt1=self.canvas.create_text(100, 600/2-100, fill='lightgreen', font=('times', 25), text='Maybe you \nshould \nhelp her...\n\n...I know\n she is having\n trouble on\n this level. :)')
                self.Level2Prompt1Bool=False
            self.EventCheck()
            self.player1.Fall()
            self.player2.Fall()
            self.CheckEnd()
                        
            self.canvas.update()
    
            time.sleep(0.005)
        exit(0)

    def Level2ShutDown(self):
        self.ObjectList=[]
        self.ButtonList1=[]
        self.ButtonList2=[]
        self.PlayerList=[]
        self.WallList=[]
        self.TriggerWallList=[]
        self.ThruWallList=[]
        self.Level3Start()
        
#==========================================================================================
    def Level3Start(self):
        self.GameProgress='Level3Start'
        self.canvas.delete(self.StartImage)
                    
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Start_Screen2.gif")
        self.Level3StartImage=self.canvas.create_image(0, 0, anchor=NW, image=self.StartImageFile)
        self.Level3StartText1=self.canvas.create_text(900/2, 600/2, fill='lightgreen', font=('times', 40), text='Level 3')
        self.Level3StartText2=self.canvas.create_text(900/2, 600/2+50, fill='lightgreen', font=('times', 40), text='Press Space to Continue')
        self.canvas.update()
        while 1:
            self.EventCheck()
            self.canvas.update()

    def Level3Startup(self):
            self.GameProgress='Level3Startup'
            self.canvas.delete(self.Level2StartImage)
            self.canvas.delete(self.Level2StartText1)
            self.canvas.delete(self.Level2StartText2)
            
            self.PlayImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\PlayBackground.gif")
            self.canvas.create_image(1, 1, anchor=NW, image=self.PlayImageFile)

            self.player1=Player1(45, 500)
            self.ObjectList.append(self.player1)
            self.PlayerList.append(self.player1)

            self.player2=Player2(70, 500)
            self.ObjectList.append(self.player2)
            self.PlayerList.append(self.player2)
            
            self.wall1=Wall(0,570, 899, 599)#Bottom Side
            self.ObjectList.append(self.wall1)
            self.WallList.append(self.wall1)

            self.wall2=Wall(0,0, 30, 599)#Left Side
            self.ObjectList.append(self.wall2)
            self.WallList.append(self.wall2)

            self.wall3=Wall(0,0, 899, 200)#Top Side
            self.ObjectList.append(self.wall3)
            self.WallList.append(self.wall3)

            self.wall4=Wall(880,0, 899, 600)#Right Side
            self.ObjectList.append(self.wall4)
            self.WallList.append(self.wall4)

            self.thruwall1=ThruWall(200,490, 220, 570)#Thru Wall
            self.ThruWallList.append(self.thruwall1)

            self.wall5=Wall(180, 480, 600, 490)#Middle Main Platform
            self.ObjectList.append(self.wall5)
            self.WallList.append(self.wall5)

            self.wall6=Wall(330, 490, 600, 570)#
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall6=Wall(600, 530, 700, 570)#
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.triggerwall1=TriggerWall(780, 201, 790, 569, True)# cover end
            self.ObjectList.append(self.triggerwall1)
            self.TriggerWallList.append(self.triggerwall1)
            self.triggerwall1remove=True

            self.triggerwall2=TriggerWall(200, 201, 210, 479, True)
            self.ObjectList.append(self.triggerwall2)
            self.TriggerWallList.append(self.triggerwall2)
            self.triggerwall2remove=True

            self.button1p2=Button(280, 465, 'triggerwall1', 2)#toggle end
            self.ButtonList2.append(self.button1p2)

            self.button1p1=Button(280, 556, 'triggerwall2', 2)#Button
            self.ButtonList1.append(self.button1p1)


            self.EndLocation=[900-60, 430+3, 880, 570]
            EndImage=self.canvas.create_rectangle(900-85, 430+3, 880-2, 570-2, outline="red", stipple="gray50", width=4)
            
            self.Level3Loop()
        
    def Level3Loop(self):
        self.GameProgress='Level3Loop'
        while self.Play==True:
            self.EventCheck()
            self.player1.Fall()
            self.player2.Fall()
            self.CheckEnd()

            Button.ButtonCheck()
            
            self.canvas.update()
            time.sleep(0.005)
        exit(0)

    def Level3ShutDown(self):
        self.ObjectList=[]
        self.ButtonList1=[]
        self.ButtonList2=[]
        self.PlayerList=[]
        self.WallList=[]
        self.TriggerWallList=[]
        self.ThruWallList=[]
        self.Level4Start()
#==========================================================================================
    def Level4Start(self):
        self.GameProgress='Level4Start'
        self.canvas.delete(self.StartImage)
                    
        self.StartImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\Start_Screen2.gif")
        self.Level1StartImage=self.canvas.create_image(0, 0, anchor=NW, image=self.StartImageFile)
        self.Level1StartText1=self.canvas.create_text(900/2, 600/2, fill='lightgreen', font=('times', 40), text='Level 4')
        self.Level1StartText2=self.canvas.create_text(900/2, 600/2+50, fill='lightgreen', font=('times', 40), text='Press Space to Continue')
        self.canvas.update()
        while 1:
            self.EventCheck()
            self.canvas.update()

    def Level4Startup(self):
            self.GameProgress='Level4Startup'
            #self.canvas.delete(self.Level3StartImage)
            #self.canvas.delete(self.Level3StartText1)
            #self.canvas.delete(self.Level3StartText2)
            
            self.PlayImageFile=PhotoImage(file="C:\\Users\\Conner\\Desktop\\Programming\\Python\\Programs\\Platformer-V1.0.0\\PlayBackground.gif")
            self.canvas.create_image(1, 1, anchor=NW, image=self.PlayImageFile)

            self.player1=Player1(900/2-110, 50)
            self.ObjectList.append(self.player1)
            self.PlayerList.append(self.player1)

            self.player2=Player2(900/2-80, 50)
            self.ObjectList.append(self.player2)
            self.PlayerList.append(self.player2)
            
            self.wall1=Wall(0,570, 899, 599)#Botoom Side
            self.ObjectList.append(self.wall1)
            self.WallList.append(self.wall1)

            self.wall2=Wall(0,0, 30, 599)#Left Side
            self.ObjectList.append(self.wall2)
            self.WallList.append(self.wall2)

            self.wall3=Wall(0,0, 899, 30)#Top Side
            self.ObjectList.append(self.wall3)
            self.WallList.append(self.wall3)

            self.wall4=Wall(885,0, 899, 599)#Right Side
            self.ObjectList.append(self.wall4)
            self.WallList.append(self.wall4)
            
            self.wall5=Wall(0,0, 180, 430)#Drop-Down Left
            self.ObjectList.append(self.wall5)
            self.WallList.append(self.wall5)

            self.wall5=Wall(160,0, 180, 470)#Drop-Down Left Extension Down
            self.ObjectList.append(self.wall5)
            self.WallList.append(self.wall5)

            self.wall6=Wall(280, 100, 400, 110)#Start Platform
            self.ObjectList.append(self.wall6)
            self.WallList.append(self.wall6)

            self.wall7=Wall(500, 0, 550, 470)#Drop-Down Right
            self.ObjectList.append(self.wall7)
            self.WallList.append(self.wall7)

            self.wall8=Wall(800, 410, 900, 600)#Right Platform
            self.ObjectList.append(self.wall8)
            self.WallList.append(self.wall8)

            self.wall8=Wall(800, 200, 900, 220)#Right Platform Up
            self.ObjectList.append(self.wall8)
            self.WallList.append(self.wall8)

            self.thruwall1=ThruWall(160, 471, 180, 570)
            self.ThruWallList.append(self.thruwall1)

            self.triggerwall1=TriggerWall(550, 300, 700, 320, False)# platform
            #self.ObjectList.append(self.triggerwall1)
            #self.TriggerWallList.append(self.triggerwall1)
            self.triggerwall1add=True

            self.triggerwall2=TriggerWall(280, 480, 420, 490, True)# cover end top
            self.ObjectList.append(self.triggerwall2)
            self.TriggerWallList.append(self.triggerwall2)
            
            self.triggerwall3=TriggerWall(280, 490, 290, 568, True)# cover end left
            self.ObjectList.append(self.triggerwall3)
            self.TriggerWallList.append(self.triggerwall3)
            
            self.triggerwall4=TriggerWall(410, 490, 420, 568, True)# cover end right
            self.ObjectList.append(self.triggerwall4)
            self.TriggerWallList.append(self.triggerwall4)
            self.triggerwall234remove=True

            self.button1p1=Button(100, 556, 'triggerwall1', 1)#Button
            self.ButtonList1.append(self.button1p1)

            self.button1p2=Button(850, 185, 'triggerwall234', 2)#Button #uncover end
            self.ButtonList2.append(self.button1p2)

            self.EndLocation=[300, 500, 400, 600]
            EndImage=self.canvas.create_rectangle(300, 500, 400, 570-2, outline="red", stipple="gray50", width=4)
            
            self.Level4Loop()
        
    def Level4Loop(self):
        self.GameProgress='Level4Loop'
        while self.Play==True:
            self.EventCheck()
            self.player1.Fall()
            self.player2.Fall()
            self.CheckEnd()

            Button.ButtonCheck()
                        
            self.canvas.update()
            time.sleep(0.005)
        exit(0)

    def Level4ShutDown(self):
        self.ObjectList=[]
        self.ButtonList1=[]
        self.ButtonList2=[]
        self.PlayerList=[]
        self.WallList=[]
        self.TriggerWallList=[]
        self.ThruWallList=[]
        self.Level4Start()
        
#==========================================================================================
        
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
            self.VelosityY=self.JumpSpeed
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
            self.Image=Main.canvas.create_rectangle(self.CoordsX1, self.CoordsY1, self.CoordsX2, self.CoordsY2, outline='lightgreen', stipple='gray50', width=3)
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
        if Main.GameProgress=='Level3Loop':
            if Main.player2.ButtonCheck()=='triggerwall1' and Main.triggerwall1remove:
                Main.ObjectList.remove(Main.triggerwall1)
                Main.TriggerWallList.remove(Main.triggerwall1)
                Main.triggerwall1remove=False
                Main.canvas.delete(Main.triggerwall1.Image)
                Main.canvas.itemconfig(Main.triggerwall1.Image, image=Main.canvas.create_rectangle(Main.triggerwall1.CoordsX1, Main.triggerwall1.CoordsY1, Main.triggerwall1.CoordsX2, Main.triggerwall1.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
            if Main.player2.ButtonCheck()=='triggerwall1': 
                Main.canvas.itemconfig(Main.button1p2.Image, image=Main.button1p2.ImageFile[3])
            else:
                Main.canvas.itemconfig(Main.button1p2.Image, image=Main.button1p2.ImageFile[2])
#-------------------------------------------------------------------------------------------------------------
            if Main.player1.ButtonCheck()=='triggerwall2' and Main.triggerwall2remove:
                Main.ObjectList.remove(Main.triggerwall2)
                Main.TriggerWallList.remove(Main.triggerwall2)
                Main.triggerwall2remove=False
                Main.canvas.delete(Main.triggerwall2.Image)
                Main.canvas.itemconfig(Main.triggerwall2.Image, image=Main.canvas.create_rectangle(Main.triggerwall2.CoordsX1, Main.triggerwall2.CoordsY1, Main.triggerwall2.CoordsX2, Main.triggerwall2.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
            if Main.player1.ButtonCheck()=='triggerwall2': 
                Main.canvas.itemconfig(Main.button1p1.Image, image=Main.button1p1.ImageFile[1])
            else:
                Main.canvas.itemconfig(Main.button1p1.Image, image=Main.button1p1.ImageFile[0])
#-------------------------------------------------------------------------------------------------------------                
        if Main.GameProgress=='Level4Loop':
            if Main.player1.ButtonCheck()=='triggerwall1' and Main.triggerwall1add:
                Main.ObjectList.append(Main.triggerwall1)
                Main.TriggerWallList.append(Main.triggerwall1)
                Main.triggerwall1add=False
                Main.canvas.delete(Main.triggerwall1.Image)
                Main.canvas.itemconfig(Main.triggerwall1.Image, image=Main.canvas.create_rectangle(Main.triggerwall1.CoordsX1, Main.triggerwall1.CoordsY1, Main.triggerwall1.CoordsX2, Main.triggerwall1.CoordsY2, fill='lightgreen', outline='lightgreen'))#, stipple='gray50', width=3))
            if Main.player1.ButtonCheck()=='triggerwall1': 
                Main.canvas.itemconfig(Main.button1p1.Image, image=Main.button1p1.ImageFile[1])
            else:
                Main.canvas.itemconfig(Main.button1p1.Image, image=Main.button1p1.ImageFile[0])
#-------------------------------------------------------------------------------------------------------------   
            if Main.player2.ButtonCheck()=='triggerwall234' and Main.triggerwall234remove:
                Main.ObjectList.remove(Main.triggerwall2)
                Main.ObjectList.remove(Main.triggerwall3)
                Main.ObjectList.remove(Main.triggerwall4)
                Main.TriggerWallList.remove(Main.triggerwall2)
                Main.TriggerWallList.remove(Main.triggerwall3)
                Main.TriggerWallList.remove(Main.triggerwall4)
                Main.triggerwall234remove=False
                Main.canvas.delete(Main.triggerwall2.Image)
                Main.canvas.delete(Main.triggerwall3.Image)
                Main.canvas.delete(Main.triggerwall4.Image)
                Main.canvas.itemconfig(Main.triggerwall2.Image, image=Main.canvas.create_rectangle(Main.triggerwall2.CoordsX1, Main.triggerwall2.CoordsY1, Main.triggerwall2.CoordsX2, Main.triggerwall2.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
                Main.canvas.itemconfig(Main.triggerwall3.Image, image=Main.canvas.create_rectangle(Main.triggerwall3.CoordsX1, Main.triggerwall3.CoordsY1, Main.triggerwall3.CoordsX2, Main.triggerwall3.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
                Main.canvas.itemconfig(Main.triggerwall4.Image, image=Main.canvas.create_rectangle(Main.triggerwall4.CoordsX1, Main.triggerwall4.CoordsY1, Main.triggerwall4.CoordsX2, Main.triggerwall4.CoordsY2, outline='lightgreen', stipple='gray50', width=3))
            if Main.player2.ButtonCheck()=='triggerwall234': 
                Main.canvas.itemconfig(Main.button1p2.Image, image=Main.button1p2.ImageFile[3])
            else:
                Main.canvas.itemconfig(Main.button1p2.Image, image=Main.button1p2.ImageFile[2])
#---------------------------------------------------------------------------------------------------

################################################################################
################################################################################        
class Player1(Players):
    def __init__(self, PosX, PosY):
        self.JumpSpeed=-1.5
        self.VelosityY=0
        self.VelosityX=0
        self.FallSpeed=0
        self.State='Standing'
        self.StateLift=False
        self.PosX=PosX
        self.PosY=PosY
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
    def __init__(self, PosX, PosY):
        self.JumpSpeed=-2.1
        self.VelosityY=0
        self.VelosityX=0
        self.FallSpeed=0
        self.State='Standing'
        self.StateLift=False
        self.PosX=PosX
        self.PosY=PosY
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
Main=Main(Width=900, Height=600, Title='Platformer V1.2.5')
Main.MainStartup()
