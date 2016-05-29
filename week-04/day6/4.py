# 4. Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).
#
# def powerN(x,y):
#     power = x ** y
#     return power
#
# print(powerN(6,7))

def powerN(x, y):
    if y == 0:
        return 1
    elif x == 0:
        return 0
    else:
        return powerN(x, y - 1) * x

print(powerN(6,7))
