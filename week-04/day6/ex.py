from tkinter import *

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

def fractal(x, y, size):
    canvas.create_oval(x, y, x+size, y+size, fill="yellow")
    if size < 10:
        pass
    else:
        fractal(x, y, size/3)
        fractal(x+size/3, y+size/3, size/3)

fractal(5, 5, 590)

root.mainloop()
