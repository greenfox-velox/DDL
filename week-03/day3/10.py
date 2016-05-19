# Create a function that prints a triangle like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#
# It should take a number as parameter that describes how many lines the triangle has

def xmas_tree(row):
    space = row - 1
    star=1
    for i in range(0, row):
        for i in range(0 , space):
            print(' ',end='')
        for i in range(0, star):
            print('*',end='')
        for i in range(0, space):
            print(' ',end='')
        star = star + 2
        space = space - 1
        print()
xmas_tree(10)
