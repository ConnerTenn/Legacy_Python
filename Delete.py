#Imports
import copy
from tkinter import *

#Variables
play=True
list1=['left']
list2=[]
final=[]
Nangle=0
Edges=[]
Direction='up'
length=int(input("iteration:"))-2
zoom=int(input("zoom:"))

#Functions
def Add_Edges(x1,y1,x2,y2,angle):
    Edges.append([x1,y1,x2,y2,angle])

def Center_Change(list2):
    if list2[int(((len(list2))/2)-0.5)] == 'left':
        list2[int(((len(list2))/2)-0.5)] = 'right'
    elif list2[int(((len(list2))/2)-0.5)] == 'right':
        list2[int(((len(list2))/2)-0.5)] = 'left'

def List_Gen():
    global list1
    for x in range(0,length):
        list2=copy.copy(list1)
        Center_Change(list2)
        list1.append('left')
        list1=copy.copy(list1+list2)
    final=copy.copy(list1)
    global final

def Canvas_Gen():
    global final
    i=0
    
    for x in final:
        i=i+1

        if x=='left':
            Nangle=Edges[i-1][4]-90
        if x=='right':
            Nangle=Edges[i-1][4]+90

        if Nangle==-90:
            Direction=270
        elif Nangle==360:
            Direction=0
        else:
            Direction=Nangle
        
        px2=Edges[i-1][2]
        py2=Edges[i-1][3]

        if Direction==0:
            x1=px2
            y1=py2
            x2=px2
            y2=py2-zoom
        if Direction==270:
            x1=px2
            y1=py2
            x2=px2-zoom
            y2=py2
        if Direction==180:
            x1=px2
            y1=py2
            x2=px2
            y2=py2+zoom
        if Direction==90:
            x1=px2
            y1=py2
            x2=px2+zoom
            y2=py2
        
        Add_Edges(x1,y1,x2,y2,Direction)

def Draw():
    i=0
    for x in Edges:
        if i==0:
            colour='red'
        else:
            colour='black'
        dx1=Edges[i][0]
        dy1=Edges[i][1]
        dx2=Edges[i][2]
        dy2=Edges[i][3]
        canvas.create_line(dx1,dy1,dx2,dy2,fill=colour)
        i=i+1        

def Main():
    print("Starting Setup!")
    '''grid=[[0 for x in range(0,10000)]for x in range(0,10000)]'''
    Edges=[[0 for x in range(0,5)]for x in range(0,0)]
    Add_Edges(500,500,500+zoom,500,90)
    print("Done Setup!")
    List_Gen()
    print("List Generated!")
    Canvas_Gen()
    print("Canvas List Generated!")
    Draw()
    print("Done!")

def Clear():
    canvas.delete("all")
#Start
tk=Tk()
canvas=Canvas(tk, width=1000, height=1000)
canvas.pack()

#Program
Main()
while play==True:
    break
