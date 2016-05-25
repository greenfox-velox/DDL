from tkinter import *

root = Tk()

canvas_width= 300
canvas_height= 300

canvas = Canvas(root, width = canvas_width, height = canvas_height)
canvas.pack()

x = 10
y = 1.5
for i in range(1, 7):
    rect = canvas.create_rectangle((1+x*y), (1+x*y), (10+x*y) * y, (10+x*y)* y, fill='purple')
    x += 20
    x += 1.5

root.mainloop()
