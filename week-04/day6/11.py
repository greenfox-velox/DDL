from tkinter import *

root = Tk()

canvas_width = 600
canvas_height = 600

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

def draw_rectangle(x,y,s):
    canvas.create_rectangle(x, y, x+s, y+s, fill='olive')

def draw_fractal(x,y,size):
    draw_rectangle(x,y,size)
    third = size//3
    if size > 5:
        draw_fractal(x + third, y, third)
        draw_fractal(x + third, y + 2 * third, third)
        draw_fractal(x, y + third, third)
        draw_fractal(x + 2*third, y + third, third)


draw_fractal(10,10,500)

root.mainloop()
