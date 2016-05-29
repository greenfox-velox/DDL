# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

def draw_square(x, y):
    rect = canvas.create_rectangle(x, y, x + 50, y + 50, fill = 'olive')

draw_square(20, 40)
draw_square(150, 150)
draw_square(220, 240)

root.mainloop()
