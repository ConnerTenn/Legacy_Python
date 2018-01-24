#Imports
from tkinter import *
import random

#Classes

############################################################################
class Main:
    def __init__(self, Width=500, Height=400, Title="Python Program"):
        self.Width=Width
        self.Height=Height
        self.Title=Title

        self.Play=True
        self.GetInput=True
        self.Response=''

        self.tk=Tk()
        self.tk.title(self.Title)
        self.tk.resizable(0,0)
        self.canvas=Canvas(self.tk, width=self.Width, height=self.Height)
        self.canvas.pack()

        self.Text=self.canvas.create_text(300/2, 900/2, font=('times', 10), text='')

#---------------------------------------------------------------------------

        self.KeyBindings=['q', 'a', 's', 'd']
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
        if self.Pressed['a']==True:
            self.Response='WaitA'
        if self.Response == 'WaitA' and self.Pressed['a']==False:
            self.Response='Correct'
            self.GetInput=False

        if self.Pressed['s']==True:
            self.Response='WaitS'
        if self.Response == 'WaitS' and self.Pressed['s']==False:
            self.Response='Good'
            self.GetInput=False
            
        if self.Pressed['d']==True:
            self.Response='WaitD'
        if self.Response == 'WaitD' and self.Pressed['d']==False:
            self.Response='Wrong'
            self.GetInput=False
            
################################################################################

    def End(self):
        self.Play=False
        
    def StartUp(self):
        Main.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.GetInput=True
            Numbers.Generate()
            
            self.canvas.itemconfig(self.Text, text=(str(Numbers.ReturnNumberList[0])+str(Numbers.ReturnNumberList[1])))
            print()
            print('Guess: %s' %(str(Numbers.ReturnNumberList[0])+str(Numbers.ReturnNumberList[1])))
            print('Wrong: %s' % Numbers.WrongList)
            print('Unused: %s' % Numbers.UnusedList)
            print('Correct: %s' % Numbers.CorrectListValues)
            while self.GetInput:
                self.EventCheck()
                self.canvas.update()
            print('Answer=%s' % self.Response)
            if self.Response=='Good':
                if Numbers.ReturnNumberList[0] in Numbers.UnusedList:
                    Numbers.UnusedList.remove(Numbers.ReturnNumberList[0])
                if Numbers.ReturnNumberList[1] in Numbers.UnusedList:
                    Numbers.UnusedList.remove(Numbers.ReturnNumberList[1])
                    
                if Numbers.CorrectListValues[Numbers.ReturnNumberList[0]] in Numbers.CorrectListValues:
                        Numbers.CorrectListValues[Numbers.ReturnNumberList[0]] = Numbers.CorrectListValues[Numbers.ReturnNumberList[0]] + 1
                if Numbers.CorrectListValues[Numbers.ReturnNumberList[1]] in Numbers.CorrectListValues:
                    Numbers.CorrectListValues[Numbers.ReturnNumberList[1]] = Numbers.CorrectListValues[Numbers.ReturnNumberList[1]] + 1
            if self.Response=='Wrong':    
                if Numbers.ReturnNumberList[0] in Numbers.UnusedList:
                    Numbers.UnusedList.remove(Numbers.ReturnNumberList[0])
                if Numbers.ReturnNumberList[1] in Numbers.UnusedList:
                    Numbers.UnusedList.remove(Numbers.ReturnNumberList[1])

                if Numbers.CorrectListValues[Numbers.ReturnNumberList[0]] >= 1:
                    Numbers.CorrectListValues[Numbers.ReturnNumberList[0]] = Numbers.CorrectListValues[Numbers.ReturnNumberList[0]] - 1
                if Numbers.CorrectListValues[Numbers.ReturnNumberList[1]] >= 1:
                    Numbers.CorrectListValues[Numbers.ReturnNumberList[1]] = Numbers.CorrectListValues[Numbers.ReturnNumberList[1]] - 1
                    
                if Numbers.ReturnNumberList[0] not in Numbers.WrongList:
                    Numbers.WrongList.append(Numbers.ReturnNumberList[0])
                if Numbers.ReturnNumberList[1] not in Numbers.WrongList:
                    Numbers.WrongList.append(Numbers.ReturnNumberList[1])
            if self.Response=='Correct':
                exit(0)
        exit(0)

################################################################################
################################################################################
class Numbers:
    def __init__(self):
        self.CorrectListValues={0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
        self.WrongList=[]
        self.UnusedList=[0,1,2,3,4,5,6,7,8,9]
        self.ReturnNumberList=[]

    def Generate(self):
        self.ReturnNumberList=[]
        if self.CorrectListCheck():
            self.ReturnNumberList.append(self.LeastCorrect())
            if len(self.UnusedList) >=1:
                self.ReturnNumberList.append(random.choice(self.UnusedList))
            elif len(self.WrongList) >=1:
                self.ReturnNumberList.append(random.choice(self.WrongList))
        elif len(self.WrongList) >= 1:
            self.ReturnNumberList.append(random.choice(self.WrongList))
            self.ReturnNumberList.append(random.choice(self.UnusedList))
        else:
            self.ReturnNumberList.append(random.choice(self.UnusedList))
            self.ReturnNumberList.append(random.choice(self.UnusedList))
                
            
            
    def CorrectListCheck(self):
        for Number in self.CorrectListValues:
            if self.CorrectListValues[Number] >= 1:
                return True
        return False

    def LeastCorrect(self):
        Lowest = self.CorrectListValues[0]
        LowestNumberList=[]
        for Number in self.CorrectListValues:
            if self.CorrectListValues[Number] < Lowest:
                Lowest=self.CorrectListValues[Number]
        for Number in self.CorrectListValues:
            if self.CorrectListValues[Number]==Lowest:
                LowestNumberList.append(Number)
        return random.choice(LowestNumberList)

#Start
Numbers=Numbers()
Main=Main(Height=600, Width=300)
Main.StartUp()
