#Imports
from tkinter import*
import time

#Variables
Play=True
Switch=True
Player='blue'
Width=500
Height=500
Size=40
ObjectSize=2.5
TextDistance=10
FieldWidth=4
FieldHeight=4

DotGrid=[]
for x in range(1,FieldWidth+1,1):
    for y in range(1,FieldHeight+1,1):
        DotGrid.append([x,y])

LineGrid=[]
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
            else:
                print("Entered cordinates out of play field")
                print()
                Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch)
        else:
            print("Entered cordinates already exist")
            print()
            Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height)
    else:
        print("Entered cordinates do not form a line or the line is too long")
        print()
        Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height)
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
    print(MaxSquare, SquareNum)
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


def Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height):
    while Play:
        NewX1=int(input("X cordinate for start of line: "))
        NewY1=int(input("Y cordinate for start of line: "))
        NewX2=int(input("X cordinate for end of line: "))
        NewY2=int(input("Y cordinate for end of line: "))
        print()
        LineGrid=AddLine(LineGrid, NewX1, NewY1, NewX2, NewY2, Player, FieldWidth, FieldHeight, Size)
        Switch=True
        SquareGrid, Switch=CheckSquare(LineGrid, SquareGrid, FieldWidth, FieldHeight, Switch)
        DrawLine(LineGrid)
        DrawSquare(SquareGrid)
        if Switch:
            if Player=='blue':
                Player='green'
            elif Player=='green':
                Player='blue'
        canvas.update()
        CheckFin(SquareGrid, FieldWidth, FieldHeight, Width, Height)
    
#Main
DrawDots(DotGrid)
DrawNum(DotGrid, Size)
canvas.update()
Main(LineGrid, SquareGrid, Player, FieldWidth, FieldHeight, Size, Switch, Width, Height)


















