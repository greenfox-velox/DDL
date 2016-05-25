# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas_width= 300
canvas_height= 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()


x = 1
for i in range(1, 28):
    rect = canvas.create_rectangle(1+x, 1+x, 10+x, 10+x, fill='purple')
    x += 11

root.mainloop()
