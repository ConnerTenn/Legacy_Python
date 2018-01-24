#Imports
from tkinter import *
import random
import time

#Setup
tk = Tk(className='''Conner's modern art''')
canvas = Canvas(tk, width=500,height=500)
canvas.pack()

#Functions
def random_rect(width, height, fill_list):
    x1=random.randrange(width)
    y1=random.randrange(height)
    x2=random.randrange(width)
    y2=random.randrange(height)
    colour=random.choice(fill_list)
    canvas.create_rectangle(x1,y1,x2,y2,outline=colour)
    
#Program
time.sleep(1)
for loop in range(0,100):
    random_rect(500,500,['red', 'green', 'blue'])
time.sleep(1)
