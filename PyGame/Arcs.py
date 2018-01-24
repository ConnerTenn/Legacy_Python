#Imports
import pygame
import math

#Constants
PI=3.14159265358979323
TAU=2.0*PI

#Classes

############################################################################
class Main:
    def __init__(self, Size = (700, 500), Title="PyGame Basic Build"):
        self.Size = Size
        self.Title=Title

        self.Play=True
        self.PyGame = pygame
        self.PyGame.init()
        
        self.Screen = self.PyGame.display.set_mode(self.Size)
        self.PyGame.display.set_caption(self.Title)
        self.Clock = self.PyGame.time.Clock()

#---------------------------------------------------------------------------

        self.ESC=chr(self.PyGame.K_ESCAPE); self.U_ARROW = chr(self.PyGame.K_UP); self.D_ARROW = chr(self.PyGame.K_DOWN); self.R_ARROW = chr(self.PyGame.K_RIGHT); self.L_ARROW = chr(self.PyGame.K_LEFT);
        self.KeyBindings=['q', self.ESC]
        self.Pressed={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=False

#---------------------------------------------------------------------------

    def KeyPressed(self, event):
        self.Pressed[chr(event.key)]=True
        #self.Pressed[event.char]=True
        
    def KeyReleased(self, event):
        self.Pressed[chr(event.key)]=False
        #self.Pressed[event.char]=False

    def KeyHandler(self):
        if self.Pressed['q']==True or self.Pressed[self.ESC]==True:
            self.Play=False
            
    def EventHandler(self):
        for event in self.PyGame.event.get():
            if event.type == self.PyGame.QUIT:
                self.Play = False
            # == Keys ==
            if event.type == self.PyGame.KEYDOWN:
                self.KeyPressed(event)
            if event.type == self.PyGame.KEYUP:
                self.KeyReleased(event)
                
#===============================================================================

    def End(self):
        self.PyGame.quit()
        
    def StartUp(self):
        self.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.EventHandler()
            self.KeyHandler()
            self.Update()
            self.Render()
            #self._Clock.tick()
        self.End()

    def Update(self):
        pass

    def Render(self):
        self.Screen.fill((255,255,255))
        #  == Draw Code ==
        self.DrawArc(self.Screen, [200,200, 1, 1],[70,10], [0,TAU])
        self.PyGame.draw.arc(self.Screen, [0,0,0], [400, 200, 2*70, 2*70], 0, TAU, 60)
        #  == End Draw Code ==
        self.PyGame.display.flip()

    def DrawArc(self, screen, pos, radius, angle):
        for y in range(-radius[0]+pos[1],radius[0]+pos[1]):
            for x in range(-radius[0]+pos[0],radius[0]+pos[0]):
                #print("x:"+str(x)+" y:"+str(y))
                if math.sqrt(pow((x-pos[0]),2)+pow((y-pos[1]),2)) <= radius[0] and\
                   math.sqrt(pow((x-pos[0]),2)+pow((y-pos[1]),2)) >= radius[1]:
                    self.PyGame.draw.rect(screen, [0,0,0], [x,y,2,2])
                    #print("A")

################################################################################

#Start
Main=Main()
Main.StartUp()
