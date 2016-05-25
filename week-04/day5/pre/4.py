from tkinter import *

canvas_width = 190
canvas_height =150

master = Tk()

w = Canvas(master, width = canvas_width, height = canvas_height)

w.pack()

w.create_oval(50, 50, 100, 100)

def circle(canvas,x,y, r):
   id = canvas.create_oval(x-r,y-r,x+r,y+r)
   return id

circle(w, 23, 32, 35)

master.mainloop()
