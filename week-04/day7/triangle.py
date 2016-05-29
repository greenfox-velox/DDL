from tkinter import *
import math

root = Tk()

canvas = Canvas(root, width = 600, height = 600)
canvas.pack()


def draw_polygon(x,y,s):
    h =  math.sqrt(3) / 2 * s
    canvas.create_polygon(x, y, x + s, y, x + s / 2, y + h , fill='olive', outline='black')

def draw_fractal(x, y, s):
    h =  math.sqrt(3) / 2 * s
    draw_polygon(x, y, s)
    half = s // 2
    if s < 5:
        pass
    else:
        draw_fractal(x, y, half)
        draw_fractal(x + half, y, half)
        draw_fractal(x + half / 2, y + h / 2, half)

draw_fractal(1, 1, 600)
root.mainloop()
