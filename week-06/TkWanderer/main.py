from tkinter import *
from gameboard import *
from character import *

def main():

    root = Tk()
    canvas_width = 720
    canvas_height = 720
    canvas = Canvas (root, width = canvas_width, height = canvas_height)
    canvas.pack()

    map_matrix =[[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 0, 0, 1, 0, 0, 0, 0]]



    level1 = GameBoard(canvas, map_matrix)
    level1.create_field()
    level1.create_board()
    hero = Hero(0,0, canvas, map_matrix)
    hero.draw_hero_default()
    root.bind('<Down>', hero.draw_hero_down)
    root.bind('<Up>', hero.draw_hero_up)
    root.bind('<Left>', hero.draw_hero_left)
    root.bind('<Right>', hero.draw_hero_right)

    boss = Boss(6,0, canvas, map_matrix)
    boss.draw_boss()

    skeleton1 = Skeleton(0 , 3, canvas, map_matrix)
    skeleton1.draw_skeleton()

    skeleton2 = Skeleton(4 , 6, canvas, map_matrix)
    skeleton2.draw_skeleton()

    skeleton3 = Skeleton(9 , 6, canvas, map_matrix)
    skeleton3.draw_skeleton()


    root.mainloop()

main()
