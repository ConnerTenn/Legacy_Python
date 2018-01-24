from tkinter import *

tk = Tk()
global LineGrid
LineGrid=['1']

def callback(event):
    canvas.create_rectangle(event.x-1, event.y-1, event.x+1, event.y+1, fill='black')
    print("clicked at", event.x, event.y)
    canvas.update()

def clear(event):
    if event.keysym=='c':
        print(LineGrid)
        
canvas = Canvas(tk, width=100, height=100)
canvas.pack()
canvas.bind_all('<KeyPress-c>', clear)
canvas.bind_all("<Button-1>", callback)


#root.mainloop()
