# Create a function that prints a diamond like this:
#       *
#      ***
#     *****
#    *******
#   *********
#  ***********
#   *********
#    *******
#     *****
#      ***
#       *
#
# It should take a number as parameter that describes how many lines the diamond has

def diamond(row):
    for i in range(row):
        for s in range (row - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()
    for i in range(row, 0, -1):
        for s in range (row - i) :
            print(" ", end="")
        for j in range((i * 2) - 1):
            print("*", end="")
        print()
diamond(10)
