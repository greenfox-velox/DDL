from tkinter import *
from random import randint

class Character():
    def __init__(self, x, y, canvas, map_matrix):
        self.x = x
        self.y = y
        self.canvas = canvas
        self.map_matrix = map_matrix

    def draw_character(self, img):
        self.canvas.create_image(self.x * 72 , self.y * 72, image = self.img, anchor = 'nw')

class Hero(Character):
    def __init__(self, x, y, canvas, map_matrix):
        super().__init__(0, 0, canvas, map_matrix)

    def draw_hero_default(self):
        self.img = PhotoImage(file= 'hero-down.png')
        super().draw_character(self.img)

    def draw_hero_down(self, event):
        self.img = PhotoImage(file= 'hero-down.png')
        if self.y + 1 <= 9:
            if self.map_matrix[self.y+1][self.x] == 0:
                self.y += 1
        super().draw_character(self.img)

    def draw_hero_up(self, event):
        self.img = PhotoImage(file= 'hero-up.png')
        if self.y - 1 >= 0:
            if self.map_matrix[self.y-1][self.x] == 0:
                self.y -= 1
        super().draw_character(self.img)

    def draw_hero_left(self, event):
        self.img = PhotoImage(file= 'hero-left.png')
        if self.x - 1 >= 0:
            if self.map_matrix[self.y][self.x-1] == 0:
                self.x -= 1
        super().draw_character(self.img)

    def draw_hero_right(self, event):
        self.img = PhotoImage(file= 'hero-right.png')
        if self.x + 1 <=9:
            if self.map_matrix[self.y][self.x + 1] == 0:
                self.x += 1
        super().draw_character(self.img)


class Monster(Character):
    def __init__(self, x, y, canvas, map_matrix):
        super().__init__(x, y, canvas, map_matrix)

    def draw_character(self, img, size= 72):
        self.size = size
        self.canvas.create_image(self.x * self.size , self.y * self.size, image = self.img, anchor = 'nw')



class Boss(Monster):
    def __init__(self, x, y, canvas, map_matrix):
        super().__init__(x, y, canvas, map_matrix)

    def draw_boss(self):
        self.img = PhotoImage(file= 'boss.png')
        super().draw_character(self.img)

class Skeleton(Monster):
    def __init__(self, x, y, canvas, map_matrix):
        super().__init__(x , y, canvas, map_matrix)

    def draw_skeleton(self):
        self.img = PhotoImage(file= 'skeleton.png')
        super().draw_character(self.img)
