# 6. We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or
# multiplication).

#
# ears = 0
#
# for i in range(123):
#     if i %2 == 0:
#         ears += 3
#     else:
#         ears += 2
# print(ears)

def ears(n):
    if n <= 0:
        return 0
    else:
        if ((n - 1)%2 == 0):
            return ears(n - 1) + 2
        else:
            return ears(n - 1) + 3

print(ears(1))
print(ears(2))
print(ears(3))
print(ears(4))
print(ears(5))
print(ears(123))
