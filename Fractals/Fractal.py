#Fractals

#Imports
import copy
import turtle

#Variables
list1=['left']
list2=[]
length=int(input("Iteration:"))-2
size=int(input("Zoom:"))
angle=90
#Functions
def iteration():
    if list2[int(((len(list2))/2)-0.5)] == 'left':
        list2[int(((len(list2))/2)-0.5)] = 'right'
    elif list2[int(((len(list2))/2)-0.5)] == 'right':
        list2[int(((len(list2))/2)-0.5)] = 'left'

def draw():
    t=turtle.Pen()
    t.speed(0)
    t.forward(size)
    for x in final:
        if x=='left':
            t.left(angle)
            t.forward(size)
        elif x=='right':
            t.right(angle)
            t.forward(size)

#Program
for x in range(0,length):
    list2=copy.copy(list1)

    iteration()
        
    list1.append('left')
    
    list1=copy.copy(list1+list2)
    
final=copy.copy(list1)

draw()
print(final)






