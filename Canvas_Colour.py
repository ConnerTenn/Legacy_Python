from tkinter import *
tk=Tk()

Width=1000
Height=600

canvas = Canvas(tk, width=Width, height=Height)
canvas.pack()

def clear():
    canvas.create_rectangle(0,0,Width,Height,fill='white',outline='white')

Image=PhotoImage(file="C:\\Users\\Conner\\Desktop\\fox.gif")
canvas.create_image(0,0,anchor=NW, image=Image)



exit
