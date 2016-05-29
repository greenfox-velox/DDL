from tkinter import *

root = Tk()

canvas = Canvas(root, width = '300', height = '300' ,bg = 'white')
canvas.pack()

x = 10
y = 0
def box(y, x):
    box = canvas.create_rectangle(y, y, y + x, y + x, fill = 'purple')

for n in range(1, 7):
    y += x
    x += 10
    box(y, x)

root.mainloop()
