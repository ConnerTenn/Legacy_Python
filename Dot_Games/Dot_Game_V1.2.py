#Imports
from tkinter import*
import time

#Variables
global Play
Play=True
global Switch
Switch=True
global Player
Player='blue'
global Width
Width=500
global Height
Height=500
global Size
Size=40
global ObjectSize
ObjectSize=3
global TextDistance
TextDistance=10
global FieldWidth
FieldWidth=4
global FieldHeight
FieldHeight=4
global DotGrid
DotGrid=[]
for y in range(1,FieldHeight+1,1):
    for x in range(1,FieldWidth+1,1):
        DotGrid.append([x,y])
global LineGrid
LineGrid=[]
global SquareGrid
SquareGrid=[]

#Startup
tk=Tk()
canvas=Canvas(tk, width=Width, height=Height)
canvas.pack()

#Classes
class Players():
    def __init__(self, colour):
        self.colour=colour
    def AddLine():
        pass

#Functions
def DrawDots(DotGrid):
    for Cords in DotGrid:
        canvas.create_rectangle(Cords[0]*Size-ObjectSize,Cords[1]*Size-ObjectSize,Cords[0]*Size+ObjectSize,Cords[1]*Size+ObjectSize, fill='black')

def DrawNum(DotGrid,Size):
    num=1
    for Cords in DotGrid:
        if Cords[0]==1:
            canvas.create_text(Cords[0]*Size-TextDistance, Cords[1]*Size, text=num)
            num=num+1
    num=1
    for Cords in DotGrid:
        if Cords[1]==1:
            canvas.create_text(Cords[0]*Size, Cords[1]*Size-TextDistance, text=num)
            num=num+1
    num=None
    
def DrawLine(LineGrid):
    for Cords in LineGrid:
        canvas.create_rectangle(Cords[0]*Size-ObjectSize,Cords[1]*Size-ObjectSize,Cords[2]*Size+ObjectSize,Cords[3]*Size+ObjectSize, fill=Cords[4], outline='white')

def DrawSquare(SquareGrid):
    for Cords in SquareGrid:
        canvas.create_rectangle(Cords[0]*Size+ObjectSize,Cords[1]*Size+ObjectSize,Cords[2]*Size-ObjectSize,Cords[3]*Size-ObjectSize, fill=Cords[4], outline='white')
        
def FindGreater(x1, y1, x2, y2):
    if x1 > x2:
        Nx1=x2
        Nx2=x1
    else:
        Nx1=x1
        Nx2=x2
    if y1 > y2:
        Ny1=y2
        Ny2=y1
    else:
        Ny1=y1
        Ny2=y2
    return [Nx1, Ny1, Nx2, Ny2]
    
def AddLine(LineGrid, x1, y1, x2, y2, Player, FieldWidth, FieldHeight, Size):
    Nx1=FindGreater(x1, y1, x2, y2)[0]
    Ny1=FindGreater(x1, y1, x2, y2)[1]
    Nx2=FindGreater(x1, y1, x2, y2)[2]
    Ny2=FindGreater(x1, y1, x2, y2)[3]
    
    TestX=abs(Nx1-Nx2)
    TestY=abs(Ny1-Ny2)
    if (TestX==1 and TestY==0) or (TestX==0 and TestY==1):
        if ([Nx1, Ny1, Nx2, Ny2, 'blue']  not in LineGrid) and ([Nx1, Ny1, Nx2, Ny2, 'green']  not in LineGrid):
            if not(Nx2>FieldWidth) and not(Ny2>FieldHeight):
                LineGrid.append([Nx1, Ny1, Nx2, Ny2, Player])
#            else:
#                print("Entered cordinates out of play field")
#                print()
#                Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height, NewX1, NewY1, NewX2, NewY2)
#        else:
#            print("Entered cordinates already exist")
#            print()
#            Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height, NewX1, NewY1, NewX2, NewY2)
#    else:
#        print("Entered cordinates do not form a line or the line is too long")
#        print()
#        Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height, NewX1, NewY1, NewX2, NewY2)
    return LineGrid

def CheckSquare(LineGrid, SquareGrid, FieldWidth, FieldHeight, Switch):
    num=0
    for count in LineGrid:
        num=num+1
        LineNum=num
    for x in range(1, FieldWidth+1):
        for y in range(1, FieldHeight+1):
            if ([x,y,x+1,y,'blue'] in LineGrid) or ([x,y,x+1,y,'green'] in LineGrid):
                if ([x,y+1,x+1,y+1,'blue'] in LineGrid) or ([x,y+1,x+1,y+1,'green'] in LineGrid):
                    if ([x,y,x,y+1,'blue'] in LineGrid) or ([x,y,x,y+1,'green'] in LineGrid):
                        if ([x+1,y,x+1,y+1,'blue'] in LineGrid) or ([x+1,y,x+1,y+1,'green'] in LineGrid):
                            
                            if ([x,y,x+1,y+1,'blue'] not in SquareGrid) and ([x,y,x+1,y+1,'green'] not in SquareGrid):
                                SquareGrid.append([x, y, x+1, y+1, LineGrid[num-1][4]])
                                Switch=False
    return SquareGrid, Switch
    
def CheckFin(SquareGrid, FieldWidth, FieldHeight, Width, Height):
    SquareNum=0
    num=0
    for count in SquareGrid:
        num=num+1
        SquareNum=num
    MaxSquare=(FieldWidth-1)*(FieldHeight-1)
    if SquareNum==MaxSquare:
        Finish(SquareGrid, Width, Height)

def Finish(SquareGrid, Width, Height):
    blue=0
    green=0
    for Square in SquareGrid:
        if Square[4]=='blue':
            blue=blue+1
        if Square[4]=='green':
            green=green+1
    if blue>green:
        Winner='BLUE'
        colour='blue'
    else:
        Winner='GREEN'
        colour='green'
    canvas.create_rectangle(Width/2-170, Height/2-30, Width/2+170, Height/2+30, fill='white', outline='black')
    canvas.create_text(Width/2, Height/2, font=('times',40), text='%s WINS' % (Winner), fill=colour)
    canvas.update()



##def Main(LineGrid, SquareGrid, FieldWidth, FieldHeight, Size, Switch, Width, Height): #, NewX1, NewY1, NewX2, NewY2):
##    Click=0
##    Player='blue'
##    while Play:
##        
##        print(Click)
##        if Click==1:
##            LineGrid=AddLine(LineGrid, NewX1, NewY1, NewX2, NewY2, Player, FieldWidth, FieldHeight, Size)
##            Switch=True
##            SquareGrid, Switch=CheckSquare(LineGrid, SquareGrid, FieldWidth, FieldHeight, Switch)
##            DrawLine(LineGrid)
##            DrawSquare(SquareGrid)
##            print(Player)
##            if Switch:
##                if Player=='blue':
##                    Player='green'
##                elif Player=='green':
##                    Player='blue'
##            CheckFin(SquareGrid, FieldWidth, FieldHeight, Width, Height)
##        canvas.update()

def Event(event):
    print('Button Pressed')
    for num in range(0, (FieldWidth-1)*(FieldHeight)+3):
        if event.x<DotGrid[num+1][0]*Size and event.x>DotGrid[num][0]*Size:
            if event.y<DotGrid[num][1]*Size+ObjectSize and event.y>DotGrid[num][1]*Size-ObjectSize:

                NewX1=DotGrid[num][0]

                NewY1=DotGrid[num][1]

                NewX2=DotGrid[num+1][0]

                NewY2=DotGrid[num+1][1]

                
                LineGrid=AddLine(LineGridp, NewX1, NewY1, NewX2, NewY2, Player, FieldWidth, FieldHeight, Size)
                #LineGridp=LineGrid
                Switch=True
                SquareGrid, Switch=CheckSquare(LineGrid, SquareGrid, FieldWidth, FieldHeight, Switch)
                DrawLine(LineGrid)
                DrawSquare(SquareGrid)
                print(Player)
                if Switch:
                    if Player=='blue':
                        Player='green'
                    elif Player=='green':
                        Player='blue'
                CheckFin(SquareGrid, FieldWidth, FieldHeight, Width, Height)
                canvas.update()

                #Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height, DotGrid[num][0], DotGrid[num][1], DotGrid[num+1][0], DotGrid[num+1][1])
        #if event.y<DotGrid[num+FieldHeight][1]*Size and event.y>DotGrid[num][1]*Size:
        #    if event.x<DotGrid[num][0]*Size+ObjectSize and event.x<DotGrid[num][0]*Size-ObjectSize:
        #        pass
                #Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height, DotGrid[num][0], DotGrid[num][1], DotGrid[num+FieldHeight][0], DotGrid[num+FieldHeight][1]     

#Main
DrawDots(DotGrid)
DrawNum(DotGrid, Size)
canvas.update()
global LineGridp
LineGridp=[]
#Main(LineGrid, SquareGrid, FieldWidth, FieldHeight, Size, Switch, Width, Height)
Click=canvas.bind_all("<Button-1>", Event)

















