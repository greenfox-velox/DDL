# create a 300x300 canvas.
# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

from tkinter import *

root = Tk()

canvas_width = 300
canvas_height = 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def draw_colorful_square(square_size, fill_colour):
    x = 1
    for i in range(1, 150):
        color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'pink']
        color_list.append(fill_colour)
        for i in color_list:
            i = [i]
            rect = canvas.create_rectangle(canvas_width/2 - (square_size/2 + x), canvas_height/2 - (square_size/2 + x), canvas_width/2 + (square_size/2) + x, canvas_height/2 + (square_size/2 + x), outline=i)
            x += 2

draw_colorful_square(1, 'olive')

root.mainloop()
