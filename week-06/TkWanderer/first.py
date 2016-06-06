from tkinter import *
from PIL import Image, ImageTk

root = Tk()

canvas_width = 700
canvas_height = 700
wanderer = Canvas (root, width = canvas_width, height = canvas_height)
wanderer.pack()

x = 0
y = 0
z = canvas_width/10

image = Image.open("floor.png")
photo = ImageTk.PhotoImage(image)

def floor_left_to_right():
    for i in range(11):
        wanderer.create_image(x + z * i, y, image=photo, anchor= 'ne')

floor_left_to_right()

# n, ne, e, se, s, sw, w, nw
#
# boss = Image.open('boss.png')
# floor = Image.open('floor.png')
# herodown = Image.open('hero-down.png')
# heroleft = Image.open('hero-left.png')
# heroright = Image.open('hero-right.png')
# heroup = Image.open('hero-up.png')
# skeleton = Image.open('skeleton.png')
# wall = Image.open('wall.png')


root.mainloop()
