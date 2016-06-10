from tkinter import *
from character import *
from stats import *

class Hero(Character):
    def __init__(self, x,y):
        super().__init__(0, 0)
        self.stats = CharacterStats()

    def hero_default(self):
        self.img = PhotoImage(file = 'images/hero-down.png')
        hero_stats = self.stats.stats_hero()
        print('Hero Level 1 HP: ', hero_stats[0],  '| DP:', hero_stats[1], '| SP:', hero_stats[2])

    def hero_down(self):
        self.img = PhotoImage(file = 'images/hero-down.png')
        self.y += 1

    def hero_up(self):
        self.img = PhotoImage(file = 'images/hero-up.png')
        self.y -= 1

    def hero_left(self):
        self.img = PhotoImage(file = 'images/hero-left.png')
        self.x -= 1

    def hero_right(self):
        self.img = PhotoImage(file = 'images/hero-right.png')
        self.x += 1
