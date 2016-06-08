from tile import *

class GameBoard(object):
    def __init__(self, canvas, input_field):
        self.canvas = canvas
        self.input_field = input_field


    def create_field(self):
        self.field = []
        for i in range(len(self.input_field)):
            for j in range(len(self.input_field[i])):
                if self.input_field[i][j] == 0:
                    self.field.append(Floor(i,j))
                else:
                    self.field.append(Wall(i,j))

    def create_board(self):
        for i in self.field:
            i.draw(self.canvas)
