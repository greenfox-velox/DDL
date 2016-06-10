from tkinter import *

class Tile():
    def __init__(self, x ,y, size= 72):
        self.size = size
        self.x = x
        self.y = y

    def draw(self, canvas):
        canvas.create_image(self.y*self.size, self.x*self.size, image=self.img, anchor=NW)

class Floor(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = PhotoImage(file='images/floor.png')


class Wall(Tile):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.img = PhotoImage(file='images/wall.png')
