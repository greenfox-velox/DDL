from tkinter import *

class Character():
    def __init__(self, x, y, size= 72):
        self.size = size
        self.x=x
        self.y=y

    def draw(self, canvas):
        canvas.create_image(self.x*self.size,self.y*self.size ,image=self.img, anchor=NW)
