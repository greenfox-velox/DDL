from tkinter import *

root = Tk()
canvas_width = 720
canvas_height = 720
canvas = Canvas (root, width = canvas_width, height = canvas_height)
canvas.pack()


image_floor = PhotoImage(file= 'floor.png')
image_wall = PhotoImage(file= 'wall.png')
image_boss = PhotoImage(file= 'boss.png')
image_herodown = PhotoImage(file= 'hero-down.png')
image_heroleft = PhotoImage(file= 'hero-left.png')
image_heroright = PhotoImage(file= 'hero-right.png')
image_heroup = PhotoImage(file= 'hero-up.png')
image_skeleton = PhotoImage(file ='skeleton.png' )


def create_wall(x, y):
    canvas.create_image(x , y, image=image_wall, anchor= 'nw')

def create_floor(x, y):
     canvas.create_image(x , y, image=image_floor, anchor= 'nw')

def create_boss(x, y):
    canvas.create_image(x , y, image=image_boss, anchor= 'nw')

def create_herodown(x, y):
    canvas.create_image(x , y, image=image_herodown, anchor= 'nw')

def create_heroleft(x, y):
     canvas.create_image(x , y, image=image_heroleft, anchor= 'nw')

def create_heroright(x, y):
    canvas.create_image(x , y, image=image_heroright, anchor= 'nw')

def create_heroup(x, y):
    canvas.create_image(x , y, image=image_heroup, anchor= 'nw')

def create_skeleton(x, y):
    canvas.create_image(x , y, image=image_skeleton, anchor= 'nw')




def return_map_int_matrix():
    map_matrix =[[0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
                [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [1, 1, 1, 1, 0, 1, 1, 1, 1, 0],
                [0, 1, 0,1, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 0]]
    return map_matrix


def create_field():
    map_matrix = return_map_int_matrix()
    for row_numbers in range(10):
        for column_numbers in range(10):
            if map_matrix[row_numbers][column_numbers] == 0:
                create_floor(column_numbers * 72, row_numbers * 72)
            else:
                create_wall(column_numbers * 72, row_numbers * 72)

def create_field_from_tile():
    map_matrix = return_map_int_matrix()
    out = []
    for row_numbers in range(10):
        for column_numbers in range(10):
            if map_matrix[row_numbers][column_numbers] == 0:
                out.append(Floor(row_numbers,column_numbers))
            else:
                out.append(Wall(row_numbers,column_numbers))
        return out




create_field()

create_herodown(0,0)
create_boss(650,650)

root.mainloop()


# create a whitebox, with black string
# print level, maxHP, currentHP, DP, SP of Hero,
# Like this: Hero (Level 1) HP: 8/10 | DP: 8 | SP: 6





# Battle
#
# when a hero enters a tile which is occupied by a monster, a battle forms
# the character entering the occupied tile is the attacker
# when the player hits space his hero strikes on the defender and then it strikes back
# the attacker strikes on the defender, then the defender strikes and this continues until one of the characters dies
# after a won battle if the character is a hero, it levels up
# Strike
#
# on a strike a strike value (SV) is calculated from SP and a d6 doubled
# the strike is successful if 2*d6 + SP is higher than the other character's DP
# on a successful strike the other character's HP is decreased by the SV - the other character's DP
# Leveling
#
# after successfully won battle the character is leveling up
# his max HP increases by d6
# his DP increases by d6
# his SP increases by d6
# Entering next area
#
# when killing the monster who held the key to the next area, the hero enters immediately
# which is like the previous one just with new and higher lvl monsters
# when entering a new area the hero has
# 10% chance to restore all his HP
# 40% chance to restore the third of his HP
# 50% chance to restore 10% of his HP
# Monster Lvl x
# HP: 2 * x * d6
# DP: x/2 * d6
# SP: x * d6
