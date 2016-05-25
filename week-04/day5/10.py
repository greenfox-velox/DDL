# create a 300x300 canvas.
# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# create a loop that draws 20 squares with that function.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width=canvas_width, height= canvas_height)
canvas.pack()

def draw_square20(square_size):
    x = 1
    for i in range(1,21):
        rect = canvas.create_rectangle(canvas_width/2 - (square_size/2 + x), canvas_height/2 - (square_size/2 + x), canvas_width/2 + (square_size/2) + x, canvas_height/2 + (square_size/2 + x))
        x += 2

draw_square20(10)

root.mainloop()
