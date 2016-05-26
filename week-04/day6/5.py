# 5. We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies
# recursively (without loops or multiplication).
#
# ears = 0
#
# for i in range(123):
#     ears += 2
# print(ears)

def ears(n):
    if n <= 0 :
        return 0
    else:
        return ears(n-1) + 2

print(ears(123))
