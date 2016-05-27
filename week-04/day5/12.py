# create a 300x300 canvas.
# fill it with a checkerboard pattern.

from tkinter import *

root = Tk()

canvas_width= 300
canvas_height= 300

canvas = Canvas(root, width= canvas_width, height= canvas_height)
canvas.pack()

x = canvas_width/8
y = canvas_height/8
z = 0


for i in range(1,9):
    if i%2 == 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, 1 * d , x+z, y, fill=c)
    z += x
z = 0
for i in range(1,9):
    if i%2 != 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, y *d , y + z, x + y*d, fill=c)
    z += x
z = 0
for i in range(1,9):
    if i%2 != 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, y *d , y + z, x + y*d, fill=c)
    z += x
z = 0
for i in range(1,9):
    if i%2 != 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, y *d , y + z, x + y*d, fill=c)
    z += x
for i in range(1,9):
    if i%2 == 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, 1 * d , x+z, y, fill=c)
    z += x
z = 0
for i in range(1,9):
    if i%2 != 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, y *d , y + z, x + y*d, fill=c)
    z += x
z = 0
for i in range(1,9):
    if i%2 != 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, y *d , y + z, x + y*d, fill=c)
    z += x
z = 0
for i in range(1,9):
    if i%2 != 0:
        c = "black"
    else:
        c = "white"
    rect = canvas.create_rectangle(1 + z, y *d , y + z, x + y*d, fill=c)
    z += x

root.mainloop()
