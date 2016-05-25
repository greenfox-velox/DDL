# create a 300x300 canvas.
# fill it with four different size and color rectangles.

from tkinter import *

root = Tk()

canvas = Canvas(root, width= 300, height= 300)
canvas.pack()

rect1 = canvas.create_rectangle(1, 1, 20, 20, fill='olive')
rect2 = canvas.create_rectangle(250, 250, 300, 300, fill='lime')
rect3 = canvas.create_rectangle(0, 300, 100, 100, fill='purple')
rect4 = canvas.create_rectangle(150, 150, 250, 175, fill='orange')

root.mainloop()
