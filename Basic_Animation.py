#Imports
import time
from tkinter import *

#Setup
tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas=Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()

#Classes
class Ball:
    def __init__(self, canvas, color):
        self.canvas = Canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
    def draw(self):
        self.canvas.move(self.id, 0, -1)

#Program
ball = Ball(tk, 'red')
while 1:
    ball.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
