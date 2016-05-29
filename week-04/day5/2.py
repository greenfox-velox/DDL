# create a 300x300 canvas.
# draw a box that has different colored lines on each edge.

from tkinter import *

root = Tk()

canvas = Canvas(root, width = 300, height = 300)
canvas.pack()

blueLine = canvas.create_line(1, 1, 1, 300, fill = 'blue')
redLine = canvas.create_line(1, 1, 300, 1, fill = 'red')
greenLine = canvas.create_line(300, 1, 300, 300, fill = 'green')
yellowLine = canvas.create_line(1, 300, 300, 300, fill = 'yellow')

root.mainloop()
