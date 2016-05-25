# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

from tkinter import *

root = Tk()
canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width= canvas_width, height= canvas_height)
canvas.pack()

def draw_line(x1, y1):
        line = canvas.create_line(x1, y1, canvas_width/2, canvas_height/2, fill= 'green')

draw_line(1, 1)
draw_line(300, 1)
draw_line(150, 1)

root.mainloop()
