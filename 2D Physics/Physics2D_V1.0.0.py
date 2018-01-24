#Imports
import pygame
import math

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
        self.KeyBindings=['q', self.ESC]
        self.Pressed={}
        for Event in self.KeyBindings:
            self.Pressed[Event]=False

#---------------------------------------------------------------------------
        self.ObjectList = []
        self.ObjectList.append(Object([[10.0, 10.0], [20.0, 20.0], [30.0, 10.0]]))
        self.ObjectList.append(Object([[110.0, 112.0], [120.0, 122.0], [130.0, 112.0]]))
        self.ObjectList.append(Object([[10.0, 50.0], [100.0, 50.0], [100.0, 60.0], [10.0, 60.0]]))
#---------------------------------------------------------------------------

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
        
    def StartUp(self):
        self.MainLoop()

    def MainLoop(self):
        while self.Play==True:
            self.EventHandler()
            self.InputHandler()
            self.Update()
            self.Render()
            self.Clock.tick(60)
        self.Shutdown()

    def Update(self):
        self.ObjectList[0].move([100,100])
        pass

    def Render(self):
        self.Screen.fill((255,255,255))
        #  == Draw Code ==
        for Obj in self.ObjectList:
            self.PyGame.draw.polygon(self.Screen, [255, 0, 0], Obj.PointList)
        #  == End Draw Code ==
        self.PyGame.display.flip()

################################################################################
class Object:
    def __init__(self, PointList = [[]]):
        self.PointList = PointList
        self.Center = [0, 0]
        for Point in self.PointList:
            self.Center[0]+=Point[0]
            self.Center[1]+=Point[1]
        self.Center[0]/=len(PointList)
        self.Center[1]/=len(PointList)
        
    def move(self, Vec):
        CollisionList = []
        for SelfPoint in self.PointList:
            for Obj in Main.ObjectList:
                if Obj != self:
                    #for ObjPoint in Obj.PointList:
                    length = len(Obj.PointList)
                    for i in range(length):
                        a=i
                        b=i+1
                        if (b == length):
                            b=0
                        #ObjLine = GetLine(Obj.PointList[a], Obj.PointList[b])
                        #print(Intersect(ObjLine, GetLine([SelfPoint[0],SelfPoint[1]],[SelfPoint[0]+Vec[0],SelfPoint[1]+Vec[1]])))
                        Result = Intersect2( [[SelfPoint[0],SelfPoint[1]],[SelfPoint[0]+Vec[0],SelfPoint[1]+Vec[1]]] , [Obj.PointList[a], Obj.PointList[b]] )
                        #print(Result)
                        if not Result == False:
                            CollisionList.append(Result)
        #if len(CollisionList) == 0:
            #print("========")
        #I = 0
        #'''
        CollisionList = sorted(CollisionList, key=lambda stu: Distance(stu[0][0]-stu[1][0],stu[0][1]-stu[1][1]))
        #print(CollisionList)
        #print()
        
        Small = 0
        I = 0
        Loop = True
        while(Loop and I < len(CollisionList)):
            Points = CollisionList[I]
            if I == 0:
                Small = Distance(Points[1][0] - Points[0][0], Points[1][1] - Points[0][1])
                Vec[0] = abs(Points[1][0] - Points[0][0])
                Vec[1] = abs(Points[1][1] - Points[0][1])
                
            else:
                if Distance(Points[1][0] - Points[0][0], Points[1][1] - Points[0][1]) == Small:
                    pass
                else:
                    Loop = False
            I += 1
        CollisionList = CollisionList[:I]
        #'''
        '''
        #Vec[0] = #abs(CollisionList[0][1][0] - CollisionList[0][0][0])
        #Vec[1] = #abs(CollisionList[0][1][1] - CollisionList[0][0][1])
        
        for Points in CollisionList:
            if Distance(Points[1][0] - Points[0][0], Points[1][1] - Points[0][1]) <= Distance(Vec[0], Vec[1]):
                Vec[0] = abs(Points[1][0] - Points[0][0])
                Vec[1] = abs(Points[1][1] - Points[0][1])
            else:
                #CollisionList.remove(Points)
                #del CollisionList[I]
                pass
            #I+=1
        '''
        self.Center[0]+=Vec[0]
        self.Center[1]+=Vec[1]
        for Point in self.PointList:
            Point[0]+=Vec[0]
            Point[1]+=Vec[1]
################################################################################
def Distance(a, b):
    return math.sqrt(math.pow(a,2)+math.pow(b,2))
def GetLine(Point1, Point2):
    a=-(Point2[1] - Point1[1])
    b=(Point2[0] - Point1[0])
    c=a*Point1[0] + b*Point1[1]
    return [a, b, c]

def Intersect(Line1, Line2):#Error: Lines are infinate
    denom = Line1[0]*Line2[1]-Line2[0]*Line1[1]
    if denom == 0:
        return False
    x=-(Line1[1]*Line2[2]-Line2[1]*Line1[2])/denom
    y=(Line1[0]*Line2[2]-Line2[0]*Line1[2])/denom
    return [x, y]
def Intersect2(LinePoints1, LinePoints2):#return collision point , original point it collided with
    #print(str(LinePoints1) + "  " + str(LinePoints2))
    Line1 = GetLine(LinePoints1[0], LinePoints1[1])
    Line2 = GetLine(LinePoints2[0], LinePoints2[1])
    
    denom = Line1[0]*Line2[1]-Line2[0]*Line1[1]
    if denom == 0:
        return False
    x=-(Line1[1]*Line2[2]-Line2[1]*Line1[2])/denom
    y=(Line1[0]*Line2[2]-Line2[0]*Line1[2])/denom
    #print("( "+str(x)+", "+str(y)+" )")
    if x >= min(LinePoints1[0][0], LinePoints1[1][0]) and x <= max(LinePoints1[0][0], LinePoints1[1][0]) and\
       y >= min(LinePoints1[0][1], LinePoints1[1][1]) and y <= max(LinePoints1[0][1], LinePoints1[1][1]) and\
       x >= min(LinePoints2[0][0], LinePoints2[1][0]) and x <= max(LinePoints2[0][0], LinePoints2[1][0]) and\
       y >= min(LinePoints2[0][1], LinePoints2[1][1]) and y <= max(LinePoints2[0][1], LinePoints2[1][1]):
        return [[x, y], [LinePoints1[0][0], LinePoints1[0][1]]]
    return False
################################################################################

#Start
Main=Main()
Main.StartUp()
