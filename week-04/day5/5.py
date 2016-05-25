# create a 300x300 canvas.
# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height =300

canvas = Canvas(root, width= canvas_width, height= canvas_height)
canvas.pack()

def draw_line2(x, y):
    line = canvas.create_line(x, y, x + 50, y, fill='green')

draw_line2(1, 1)
draw_line2(1, 150)
draw_line2(150, 1)

root.mainloop()
