# Create a function that prints a triangle like this:
#   *
#   **
#   ***
#   ****
#   *****
#   ******
# It should take a number as parameter that describes how many lines the triangle has


def triangle_of_stars(row):
    star = 1
    while (star <= row):
        print("*" * star)
        star = star + 1

triangle_of_stars(10)
