from tkinter import *


class Tile(object):
    def __init__(self, x, y, size=72):
        self.x = x
        self.y = y
        self.size = size

    def draw(self, canvas):
        canvas.create_image(self.y * self.size , self.x * self.size, image=self.img, anchor= 'nw')

class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = PhotoImage(file= 'floor.png')


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = PhotoImage(file= 'wall.png')
