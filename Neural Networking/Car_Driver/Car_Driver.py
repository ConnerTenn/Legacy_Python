#Imports
import pygame

#Constants
PI=3.14159265358979323
TAU=2.0*PI

#Classes

############################################################################
class Main:
    def __init__(self, Size = (700, 500), Title="PyGame Basic Build", ShowCursor=True):
        self.Size = Size
        self.Title=Title

        self.Play=True
        self.PyGame = pygame
        self.PyGame.init()
        
        self.Screen = self.PyGame.display.set_mode(self.Size)
        self.PyGame.display.set_caption(self.Title)
        self.PyGame.mouse.set_visible(ShowCursor)
        self.Clock = self.PyGame.time.Clock()

#---------------------------------------------------------------------------
        self.MousePos = [0,0]
        self.MouseButtons = [False, False, False]#left, right, middle
        
        self.ESC=chr(self.PyGame.K_ESCAPE); self.U_ARROW = chr(self.PyGame.K_UP); self.D_ARROW = chr(self.PyGame.K_DOWN); self.R_ARROW = chr(self.PyGame.K_RIGHT); self.L_ARROW = chr(self.PyGame.K_LEFT);
        self.KeyBindings=['q', self.ESC, 'a']
        self.Pressed={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=[False, False]
            #                   [Pressed, Key Down]

#---------------------------------------------------------------------------

    def KeyPressed(self, event):
        self.Pressed[chr(event.key)]=[True,True]
        
    def KeyReleased(self, event):
        self.Pressed[chr(event.key)]=[False, False]

    def KeyUpdate(self):
        for Key in self.KeyBindings:
            if self.Pressed[Key][1] == True:
                self.Pressed[Key][1] = False
                

    def InputHandler(self):
        self.MousePos=self.PyGame.mouse.get_pos()
        self.MouseButtons=self.PyGame.mouse.get_pressed()
        if self.Pressed['q'][0]==True or self.Pressed[self.ESC][0]==True:
            self.Play=False
            
    def EventHandler(self):
        self.KeyUpdate()
        for event in self.PyGame.event.get():
            if event.type == self.PyGame.QUIT:
                self.Play = False
            # == Keys ==
            if event.type == self.PyGame.KEYDOWN:
                self.KeyPressed(event)
            if event.type == self.PyGame.KEYUP:
                self.KeyReleased(event)
                
#===============================================================================

    def Shutdown(self):
        self.PyGame.quit()
        
    def StartUp(self):
        self.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.EventHandler()
            self.InputHandler()
            self.Update()
            self.Render()
            #self.Clock.tick()
        self.Shutdown()

    def Update(self):
        pass

    def Render(self):
        self.Screen.fill((255,255,255))
        #  == Draw Code ==

        #  == End Draw Code ==
        self.PyGame.display.flip()

################################################################################
class Car:
    pass

################################################################################
class Neuron:
    def __init__(self, Inputs):
        self.Inputs = []
        self.Weights = []
        self.Value = 0
        pass
    def Update():
        pass

class NeuronWeb:
    def __init__(self):
        self.Inputs = []
        self.Net = []
        self.Outputs = []

        self.Inputs.append(Neuron())
        self.Net.append(Neuron(self.Input[0]))
        self.Output.append(Neuron(self.Net[0]))
    def Update():
        for I in Inputs:
            
################################################################################

#Start
Main=Main()
Main.StartUp()
