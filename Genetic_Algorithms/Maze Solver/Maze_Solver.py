#Imports
import pygame
import time
import threading
import math
import DFS_maze_gen_final
import random
import copy

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
        self.Thread = threading.Thread(target=self.Update)

        self.ResetData()

#---------------------------------------------------------------------------
        self.MousePos = [0,0]
        self.MouseButtons = [False, False, False]#left, right, middle
        
        self.ESC=chr(self.PyGame.K_ESCAPE); self.U_ARROW = chr(self.PyGame.K_UP); self.D_ARROW = chr(self.PyGame.K_DOWN); self.R_ARROW = chr(self.PyGame.K_RIGHT); self.L_ARROW = chr(self.PyGame.K_LEFT);
        self.KeyBindings=['q', self.ESC]
        self.Pressed={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=False

#---------------------------------------------------------------------------

    def ResetData(self):
        self.SimulationDelay = 0.0#1
        self.MazeDimensions = [10,10]
        self.Maze = DFS_maze_gen_final.Generate(self.MazeDimensions[0], self.MazeDimensions[1])
        self.ResetMazeData(-1)
        
        self.MaxSteps = 4000
        self.PopulationSize = 100
        self.MutationRate = 0.3#05

        self.RunnerList = []
        for I in range(0, self.PopulationSize):
            self.RunnerList.append(Runner([], True))
        #self.RunnerList = [Runner()]#, Runner(), Runner()]
        #self.RunnerList[0].DNA = [[3,1,2], [1,1,0], [2,1,0]]
        #self.RunnerList[0].DNA = [[3,2,1], [1,1,0], [2,1,0]]
        #self.RunnerList[0].DNA = [[4, 1, 3, 0, 1, 5], [4, 1, 0, 0, 1, 6], [4, 1, 1, 1, 1, 3], [2, 1, 1], [1, 1, 0], [2, 3, 1], [1, 1, 0]]
        #If, Test walls around it, Direction, val, jump setting, jump val

        '''
        0 if left wall is open jump 5
        1 if forward wall is open jump 6
        2 if forward wall is closed jump 3
        3 turn right,
        4 move forward
        5 turn left,
        6 move forward
        '''
        self.Generation = 1
        self.GenerationCheck = [False, False, False]
        self.CurrentObject = 0
        self.State = ""
        self.PrintUpdates = True

    def KeyPressed(self, event):
        self.Pressed[chr(event.key)]=True
        #self.Pressed[event.char]=True
        
    def KeyReleased(self, event):
        self.Pressed[chr(event.key)]=False
        #self.Pressed[event.char]=False

    def InputHandler(self):
        self.MousePos=self.PyGame.mouse.get_pos()
        self.MouseButtons=self.PyGame.mouse.get_pressed()
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

    def Shutdown(self):
        self.PyGame.quit()
        #exit(0)
        
    def StartUp(self):
        #t = threading.Thread(target=self.Simulate)
        self.Thread.daemon = True  # thread dies when main thread (only non-daemon thread) exits.
        self.Thread.start()
        self.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.EventHandler()
            self.InputHandler()
            #self.Update()
            self.Render()
            #self.Clock.tick()
            #time.sleep(self.SimulationDelay)
        self.Shutdown()

    #def Update(self):
        #pass

    def ResetMazeData(self, val):
        #reset maze history data
        for x in range(0, self.MazeDimensions[0]):
            for y in range(0, self.MazeDimensions[1]):
                self.Maze[x][y][1] = val

    def CMD(self):
        print("=======================")
        print("1: Calculate Next Gen")
        print("2: Test")
        print("3: Kill & Crossover & Mutate")
        print("4: Auto Run")
        print("5: Settings")
        print("6: Interpret")
        print("G: God Mode")
        Selection = "1"
        Selection = input(">>").rstrip()
        if Selection == "1":
            self.State = "Simulate"
            self.Simulate()
            self.State = ""
        if Selection == "2":
            print("Enter Object to Test")
            self.CurrentObject = int(input(">>"))
            self.State = "Testing"
            self.Test()
            self.State = ""
        if Selection == "3":
            self.Kill()
            self.Crossover()
        if Selection == "4":
            print("Number of Generations")
            Selection = int(input(">>"))
            for I in range(0, Selection):
                self.State = "Simulate"
                self.Simulate()
                self.State = ""
                self.Kill()
                self.Crossover()                
        if Selection == "5":
            print("== Settings ==")
            print("1: Change Simulation Delay")
            print("2: Print Updates")
            print("3: Change Mutation Rate")
            Selection = input(">>").rstrip()
            if Selection == "1":
                print("Enter Delay (Seconds)")
                self.SimulationDelay = float(input(">>"))
            if Selection == "2":
                print("1: True,  2: False")
                Selection = input(">>").rstrip()
                if Selection == "1": self.PrintUpdates = True
                if Selection == "2": self.PrintUpdates = False
            if Selection == "3":
                print("Enter Mutation Rate (float 0-1)")
                self.MutationRate = float(input(">>"))
        if Selection == "6":
            print("Enter Object to Interpret")
            Selection = int(input(">>"))
            self.RunnerList[Selection].InterpretDNA()
        if Selection in ["G", "g"]:
            try:
                exec(input(">>"))
            except:
                print("Error:: Invalid Code")
    
    def Update(self):
        while self.Play:
            self.CMD()
        pass

    def Simulate(self, Start=0, Step=1):
        if self.PrintUpdates:
            print("Generation:" + str(self.Generation))
        self.GenerationCheck[0] = True
        #for Object in self.RunnerList:
        for self.CurrentObject in range(Start, len(self.RunnerList), Step):
            self.ResetMazeData(-1)
            Object = self.RunnerList[self.CurrentObject]
            if self.PrintUpdates:
                print("Runner:" + str(self.CurrentObject+1) + "/" + str(self.PopulationSize) +\
                        " DNA Len:" + str(len(Object.DNA)), end="")
            #print(Object.DNA)
            Object.Run(self.MaxSteps, self.Maze, self.SimulationDelay, self.MazeDimensions)
            self.ResetMazeData(-1)
            Object.GetFitness(self.Maze, self.MazeDimensions, self.MaxSteps)
            if self.PrintUpdates:
                print(" Pos"+str(Object.Pos) +\
                        " Dist:" + str(Object.DistanceFromEnd) +\
                        " Fitness: " + str(Object.Fitness))
            self.ResetMazeData(-1)
            #print("Fitness:" + str(Object.Fitness))
        #sort self.RunnerList from greatest to least by fitness
        self.RunnerList=sorted(self.RunnerList, key=lambda Object: Object.Fitness, reverse=True)

    def Test(self):
        Object = self.RunnerList[self.CurrentObject]
        if self.PrintUpdates:
            print("Runner:" + str(self.CurrentObject+1) + "/" + str(self.PopulationSize) +\
                    " DNA Len:" + str(len(Object.DNA)), end="")
        #print(Object.DNA)
        Object.Run(self.MaxSteps, self.Maze, self.SimulationDelay, self.MazeDimensions)
        if self.PrintUpdates:
            print(" Pos"+str(Object.Pos) +\
                    " Dist:" + str(Object.DistanceFromEnd) +\
                    " Fitness: " + str(Object.Fitness))
        self.ResetMazeData(-1)

    def Kill(self):
        self.GenerationCheck[1] = True
        #print(len(self.RunnerList))
        for self.CurrentObject in range(0, len(self.RunnerList)):
            if random.sample(range(0, len(self.RunnerList)),1)[0] < self.CurrentObject:
                self.RunnerList[self.CurrentObject] = -1
                #print(self.CurrentObject)
        I = 0
        while I < len(self.RunnerList):
            if self.RunnerList[I] == -1:
                self.RunnerList.remove(self.RunnerList[I])
            else:
                I += 1
        #print(len(self.RunnerList))
                
    def Crossover(self):
        self.GenerationCheck[2] = True
        while len(self.RunnerList) < self.PopulationSize:
            Sample = random.sample(self.RunnerList, 2)
            NewDNA = []
            Temp = [Sample[0].DNA, Sample[1].DNA]
            for I in range(0, Sample[0].MaxDNALen):
                Gene = []
                Selection = random.sample([0,1],1)[0]
                #test if instruction is the same type
                '''if Temp[0][I][0]==Temp[0][I][0]:
                    if Temp[0][I][0] == 4:
                        if Temp[0][I][0]
                    else:
                        Gene = Temp[Selection][I]
                else:
                    Gene = Temp[Selection][I]'''
                Gene = copy.deepcopy(Temp[Selection][I])
                NewDNA.append(Gene)
            NewRunner = Runner(NewDNA)
            NewRunner.Mutate(self.MutationRate)
            self.RunnerList.append(NewRunner)
            
        
    def Render(self):
        self.Screen.fill((255,255,255))
        #  == Draw Code ==
        if not False in self.GenerationCheck:
            self.Generation+=1
            self.GenerationCheck = [False, False, False]
        Font = self.PyGame.font.SysFont('Consolas', 25, True, False)
        Text = Font.render("Generation:"+str(self.Generation),True,[0,0,0])
        self.Screen.blit(Text, [450, 450])

        #Text = Font.render("Steps:"+str(self.RunnerList[self.CurrentObject-1].Steps),True,[0,0,0])
        #self.Screen.blit(Text, [450, 450])

        
        self.DrawMaze(self.Maze, [0,0])
        #self.DrawMaze(self.Maze, [350,0])
        #if self.Simulation:
        if self.State in ["Simulate", "Testing"]:
            self.RunnerList[self.CurrentObject].Draw(self.PyGame, self.Screen)
        #if self.State in ["Simulate"]:
        #    self.RunnerList[self.CurrentObject[1]].Draw(self.PyGame, self.Screen)
        #  == End Draw Code ==
        self.PyGame.display.flip()

    def DrawMaze(self, Maze, Offset):
        for x in range(0, self.MazeDimensions[0]*10, 10):
            for y in range(0, self.MazeDimensions[1]*10, 10):
                #print(str(x) + " "+ str(y))
                #print(self.Maze[int(x/10)][int(y/10)][1])
                if self.Maze[int(x/10)][int(y/10)][1] != -1 and self.State in ["Simulate", "Testing"]:
                    self.PyGame.draw.polygon(self.Screen, [100,255,100], [[Offset[0]+x+0, Offset[1]+y+0], [Offset[0]+x+9, Offset[1]+y+0], [Offset[0]+x+9, Offset[1]+y+9], [Offset[0]+x+0, Offset[1]+y+9]])
                
                self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+0, Offset[1]+y+0], [Offset[0]+x+2, Offset[1]+y+0], [Offset[0]+x+2, Offset[1]+y+2], [Offset[0]+x+0, Offset[1]+y+2]])
                self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+7, Offset[1]+y+0], [Offset[0]+x+9, Offset[1]+y+0], [Offset[0]+x+9, Offset[1]+y+2], [Offset[0]+x+7, Offset[1]+y+2]])
                self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+0, Offset[1]+y+7], [Offset[0]+x+2, Offset[1]+y+7], [Offset[0]+x+2, Offset[1]+y+9], [Offset[0]+x+0, Offset[1]+y+9]])
                self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+7, Offset[1]+y+7], [Offset[0]+x+9, Offset[1]+y+7], [Offset[0]+x+9, Offset[1]+y+9], [Offset[0]+x+7, Offset[1]+y+9]])

                #self.PyGame.draw.line(self.Screen, [0,0,0], [x+0, y+0], [x+9, y+0])
                #self.PyGame.draw.line(self.Screen, [0,0,0], [x+0, y+0], [x+0, y+9])
                #self.PyGame.draw.line(self.Screen, [0,0,0], [x+0, y+9], [x+9, y+9])
                #self.PyGame.draw.line(self.Screen, [0,0,0], [x+9, y+0], [x+9, y+9])
                '''
                if Maze[int(y/10)][int(x/10)][0][0]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[x+2, y+0], [x+7, y+0], [x+7, y+2], [x+2, y+2]])
                if Maze[int(y/10)][int(x/10)][0][1]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[x+7, y+0], [x+9, y+0], [x+9, y+7], [x+7, y+7]])
                if Maze[int(y/10)][int(x/10)][0][2]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[x+2, y+7], [x+7, y+7], [x+7, y+9], [x+2, y+9]])
                if Maze[int(y/10)][int(x/10)][0][3]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[x+0, y+0], [x+2, y+0], [x+2, y+7], [x+0, y+7]])
                '''
                if Maze[int(x/10)][int(y/10)][0][0]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+2, Offset[1]+y+0], [Offset[0]+x+7, Offset[1]+y+0], [Offset[0]+x+7, Offset[1]+y+2], [Offset[0]+x+2, Offset[1]+y+2]])
                if Maze[int(x/10)][int(y/10)][0][1]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+7, Offset[1]+y+0], [Offset[0]+x+9, Offset[1]+y+0], [Offset[0]+x+9, Offset[1]+y+7], [Offset[0]+x+7, Offset[1]+y+7]])
                if Maze[int(x/10)][int(y/10)][0][2]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+2, Offset[1]+y+7], [Offset[0]+x+7, Offset[1]+y+7], [Offset[0]+x+7, Offset[1]+y+9], [Offset[0]+x+2, Offset[1]+y+9]])
                if Maze[int(x/10)][int(y/10)][0][3]==1:
                    self.PyGame.draw.polygon(self.Screen, [0,0,0], [[Offset[0]+x+0, Offset[1]+y+0], [Offset[0]+x+2, Offset[1]+y+0], [Offset[0]+x+2, Offset[1]+y+7], [Offset[0]+x+0, Offset[1]+y+7]])
                

################################################################################
"""
DNA:

-Syntax:
--lists within lists for commands
--move and turn actions are one step
--restart from beginning after every step

-1: Move(amount)
--amount is number of units

-2: Turn(amount)
--amount turns by: amount/4*TAU
--positive is turn right, negative is opposite

-3: Jump(setting, amount)
--setting:
---1: abslolute
---2: reletive
--amount: lines to jump by (can be negative to go up)

-4: If (condition) { Jump(setting, amount) }:
--Syntax:
---
--Conditions:
---1: what peice is around it reletive to it's direction
----Val/8*Tau
---2: if the peice has been visited
----1: test if the peice has been visited, 0: test if not visited
---3: if a peice around it is greater or less than it's own count
----Val/8*Tau
----1: if greater, 0: if less than
---if the direction previously traveled is the same as it's current


Fitness:
-length of code
-distance to end
"""

class Runner:
    def __init__(self, DNA, Begin=False):
        self.DNA = list(DNA)
        self.MaxDNALen = 50
        if Begin:
            self.GenerateDNA()
        self.Fitness = 0

        self.ResetVars()

    def ResetVars(self):
        self.Index = 0
        self.Steps = 0
        self.Trace = 0
        self.Pos = [0,0]
        self.Direction = 1 #stored as int. Used as Direction/4 * TAU
        self.DistanceFromEnd = 0
        
    def GenerateJumpGene(self, Gene, MaxLen):
        #Setting
        Choice = random.sample([1,2],1)[0]
        Gene.append(Choice)
        #ABS
        if Choice == 1:
            Gene.append(random.sample([0, MaxLen],1)[0])
        #Reletive
        if Choice == 2:
            Gene.append(random.sample(range(-len(self.DNA), (MaxLen-len(self.DNA))+1),1)[0])
            
    def GenerateDNA(self):
        Length = random.randint(1, self.MaxDNALen)
        Length = self.MaxDNALen
        for I in range(0, Length):
            Gene = []
            Choice = random.sample([1, 2, 3, 4],1)[0]
            Gene.append(Choice)
            #Move Command
            if Choice == 1:
                #Direction
                Gene.append(random.sample([1,1,-1],1)[0])
                #Fall through
                Gene.append(random.sample([0,0,1],1)[0])
            #Turn Command
            elif Choice == 2:
                #Direction
                Gene.append(random.sample([0,1,2,3],1)[0])
                #Fall through
                Gene.append(random.sample([0,0,1],1)[0])
            #Jump Command
            elif Choice == 3:
                self.GenerateJumpGene(Gene, Length)
            #If Command
            elif Choice == 4:
                #type of test
                Choice = random.sample([1,1,1,2],1)[0]
                Gene.append(Choice)
                #test walls around it
                if Choice == 1:
                    #Direction
                    Gene.append(random.sample([0,1,2,3],1)[0])
                    #wall type to test for
                    Gene.append(random.sample([0, 1],1)[0])
                    #Generate Jump Command
                    self.GenerateJumpGene(Gene, Length)
                #test if current peice is visited
                elif Choice == 2:
                    #test if visited vs test if not visited
                    Gene.append(random.sample([1, 0],1)[0])
                    #Generate Jump Command
                    self.GenerateJumpGene(Gene, Length)
                #test value of peice around it
                elif Choice == 3:
                    #Direction
                    Gene.append(random.sample([0,1,2,3],1)[0])
                    #1:Greater 2:less than
                    Gene.append(random.sample([1, 2],1)[0])
                    #Generate Jump Command
                    self.GenerateJumpGene(Gene, Length)
                    
            self.DNA.append(Gene)
        #print(self.DNA)

    def Mutate(self, MutationRate):
        #get random genes to mutate                                         v find ceiling( 10% of the max length )
        for Index in random.sample(range(0, self.MaxDNALen), random.sample(range(0, int(self.MaxDNALen*MutationRate+1)),1)[0]):
            #print(Index)
            Gene = self.DNA[Index]
            Choice = random.sample([Gene[0],1,2,3,4],1)[0]
            Length = len(self.DNA)
            #Move Command
            if Choice == 1:
                #Direction
                Gene.append(random.sample([1,1,-1],1)[0])
                #Fall through
                Gene.append(random.sample([0,0,1],1)[0])
            #Turn Command
            elif Choice == 2:
                #Direction
                Gene.append(random.sample([0,1,2,3],1)[0])
                #Fall through
                Gene.append(random.sample([0,0,1],1)[0])
            #Jump Command
            elif Choice == 3:
                self.GenerateJumpGene(Gene, Length)
            #If Command
            elif Choice == 4:
                #type of test
                Choice = random.sample([1,1,1,2],1)[0]
                Gene.append(Choice)
                #test walls around it
                if Choice == 1:
                    #Direction
                    Gene.append(random.sample([0,1,2,3],1)[0])
                    #wall type to test for
                    Gene.append(random.sample([0, 1],1)[0])
                    #Generate Jump Command
                    self.GenerateJumpGene(Gene, Length)
                #test if current peice is visited
                elif Choice == 2:
                    #test if visited vs test if not visited
                    Gene.append(random.sample([1, 0],1)[0])
                    #Generate Jump Command
                    self.GenerateJumpGene(Gene, Length)
            self.DNA[Index] = Gene
    
    def GetFitness(self, Maze, MazeDimnesions, MaxSteps):
        self.DistanceFromEnd = self.GetDistanceFromEnd([MazeDimnesions[0]-1, MazeDimnesions[1]-1], self.Pos, Maze, 0)[0]
        #print("Pos"+str(self.Pos)+" Dist:"+str(DistanceFromEnd))
        self.Fitness = \
                       12*(1-(self.DistanceFromEnd/(MazeDimnesions[0]*MazeDimnesions[1]))) +\
                       8*(1-(self.Steps/MaxSteps))
        #0.1*(1-(len(self.DNA)-1)/(self.MaxDNALen-1)) +\

    def Move(self, Amount, Maze):
        #print("Move")
        #print(str(self.Pos) + " " + str(self.Direction))
        #print(Maze[self.Pos[0]][self.Pos[1]])
        if Maze[int(self.Pos[0])][int(self.Pos[1])][0][int(self.Direction%4)] == 0:
            self.Pos[0] += int(math.sin(self.Direction/4*TAU))
            self.Pos[1] -= int(math.cos(self.Direction/4*TAU))

    def Jump(self, Setting, Val):
        #print("Jump")
        #ABS Jump
        if Setting == 1:
            self.Index = Val
        #Reletive Jump
        if Setting == 2:
            self.Index += Val
    
    def Run(self, MaxSteps, Maze, Delay, MazeDymensions):
        #print(self.DNA)
        self.ResetVars()
        run = True
        while self.Steps < MaxSteps and run:
            self.Index=0
            while self.Index < len(self.DNA) and self.Steps < MaxSteps and run:
                #print("Steps:"+str(self.Steps))
                #print("Index:" +str(self.Index))
                Command = self.DNA[self.Index]
                #Move Command
                if Command[0] == 1:
                    Maze[self.Pos[0]][self.Pos[1]][1] = self.Trace
                    self.Trace += 1
                    self.Move(Command[1], Maze)
                    #self.Steps+=1
                    if Command[2] == 1:
                        self.Index +=1
                    else:
                        self.Index=len(self.DNA)
                    #Check if reach Finish
                    if self.Pos[0] == MazeDymensions[0]-1 and self.Pos[1] == MazeDymensions[1]-1:
                        run = False
                    time.sleep(Delay)
                #Turn Command
                elif Command[0] == 2:
                    #print("Turn")
                    self.Direction += Command[1]
                    #self.Steps+=1
                    if Command[2] == 1:
                        self.Index +=1
                    else:
                        self.Index=len(self.DNA)
                    time.sleep(Delay)
                #Jump Command
                elif Command[0] == 3:
                    self.Jump(Command[1], Command[2])
                #If Command
                elif Command[0] == 4:
                    #test walls around it
                    if Command[1] == 1:
                        #print("test walls around it")
                        if Maze[self.Pos[0]][self.Pos[1]][0][(Command[2]+self.Direction)%4] == Command[3]:
                            self.Jump(Command[4], Command[5])
                        else:
                            self.Index+=1
                    #test if current peice is visited
                    elif Command[1] == 2:
                        #Command[2]:
                        #1:if visited
                        #0:if not visited
                        #abs(1-a-True)
                        if abs(1 - Command[2] - Maze[self.Pos[0]][self.Pos[1]][1] == -1):
                            self.Jump(Command[3], Command[4])
                        else:
                            self.Index+=1
                    else:
                        self.Index +=1
                else:
                    self.Index+=1
                self.Steps+=1
                #print("Steps")
            #self.Steps+=1
            #print("Delay")
            #time.sleep(Delay)
        #print("Delay, Step")
        #time.sleep(Delay)        

    def Draw(self, PyGame, Screen):
        x=self.Pos[0]
        y=self.Pos[1]
        if self.Direction%4 == 0:
            PyGame.draw.polygon(Screen, [0,0,255], [[2+x*10, 10+y*10], [5+x*10, 0+y*10], [8+x*10, 10+y*10]])
        if self.Direction%4 == 1:
            PyGame.draw.polygon(Screen, [0,0,255], [[0+x*10, 2+y*10], [10+x*10, 5+y*10], [0+x*10, 8+y*10]])
        if self.Direction%4 == 2:
            PyGame.draw.polygon(Screen, [0,0,255], [[2+x*10, 0+y*10], [5+x*10, 10+y*10], [8+x*10, 0+y*10]])
        if self.Direction%4 == 3:
            PyGame.draw.polygon(Screen, [0,0,255], [[10+x*10, 2+y*10], [0+x*10, 5+y*10], [10+x*10, 8+y*10]])
        #PyGame.draw.rect(Screen, [0,0,0], [self.Pos[0], self.Pos[1], 10, 10])

    def InterpretJump(self, Setting, Val):
        print("Jump ",end="")
        #ABS Jump
        if Setting == 1:
            print("Abs ",end="")
            print(Val,end="")
        #Reletive Jump
        if Setting == 2:
            print("Reletive ",end="")
            print(Val,end="")
    
    def InterpretDNA(self):
        I = 0
        for Command in self.DNA:
            print(str(I)+": ",end="")
            #Move Command
            if Command[0] == 1:
                print("Move ",end="")
                print(Command[1],end="")
                if Command[2] == 1:
                    print(" Fall-through",end="")
                else:
                    print(" End",end="")
            #Turn Command
            elif Command[0] == 2:
                print("Turn ",end="")
                print(Command[1],end="")
                if Command[2] == 1:
                    print(" Fall-through",end="")
                else:
                    print(" End",end="")
            #Jump Command
            elif Command[0] == 3:
                self.InterpretJump(Command[1], Command[2])
            #If Command
            elif Command[0] == 4:
                print("Test ",end="")
                #test walls around it
                if Command[1] == 1:
                    print("Walls ",end="")
                    print("Direction:",end="")
                    print(Command[2],end="")
                    print(" Is ",end="")
                    if Command[3] == 0:
                        print("Open: ",end="")
                    if Command[3] == 1:
                        print("Wall: ",end="")
                    self.InterpretJump(Command[4], Command[5])
                #test if current peice is visited
                elif Command[1] == 2:
                    print("If Peice",end="")
                    #Command[2]:
                    #1:if visited
                    #0:if not visited
                    #abs(1-a-True)
                    if Command[2] == 1:
                        print("Visited: ",end="")
                    if Command[2] == 1:
                        print("Not-Visited: ",end="")
                    self.InterpretJump(Command[3], Command[4])
                else:
                    print("ERR:Not-Command",end="")
            else:
                print("ERR:Not-Command",end="")
            print()
            I+=1

    def GetDistanceFromEnd(self, Current, Target, Maze, Distance):
        # Structure of "database" [[dir_x,dir_y,wall_index]...]
        #inverted: start down and rotate anti-clockwise
        db = [[0,-1,0], [1,0,1], [0,1,2], [-1,0,3]]
        
        #print(str(Current)+":"+str(Distance))
        Maze[Current[0]][Current[1]][1] = 1
        if Current[0] == Target[0] and Current[1] == Target[1]:
            return [ Distance, True]
        
        #Max = [len(Maze), len(Maze[0])]
        #Neighbours = self.GetNeighbours(Current, Max, Maze)
        Neighbours = []
        for I in range(0, 4):
            if Maze[Current[0]][Current[1]][0][I] == 0:
                Neighbours.append([Current[0]+db[I][0], Current[1]+db[I][1]])
        #print("1"+str(Neighbours))
        # Removing cells that have already been visited
        i = 0
        while i < len(Neighbours):
            Cell = Neighbours[i]
            # Executes if this cell has been visited
            if Maze[Cell[0]][Cell[1]][1] == 1:
                Neighbours.remove(Cell)
            else:
                i += 1

        #random.shuffle(Neighbours)       
        for nxt in Neighbours:
            # nxt structure [row,col,wall]
            # Config. walls for 'curr' cell and 'nxt' cell
            if Maze[nxt[0]][nxt[1]][1] == 1 : continue # update
            #if nxt[0] == Target[0] and nxt[1] == Target[1]:
                #return [Distance + 1, True]
            Result = self.GetDistanceFromEnd(nxt[:2], Target, Maze, Distance+1)
            if Result[1] == True:
                return Result
            
            Result[0] -= 1
            Distance = Result[0]
        return [Distance, False]
        

################################################################################

#Start
Main=Main()
Main.StartUp()
