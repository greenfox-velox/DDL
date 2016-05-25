# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center

from tkinter import *

root = Tk()

canvas_width= 300
canvas_height= 300

canvas = Canvas(root, width= canvas_width, height= canvas_height)
canvas.pack()

def line_drawing(x, y):
    z = 0
    for i in range(1,18):
        rect = canvas.create_line(x+z, y, canvas_width/2, canvas_height/2)
        z +=20

line_drawing(1,1)

root.mainloop()
