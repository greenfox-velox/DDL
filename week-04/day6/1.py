# 1. write a recursive function
# that takes one parameter: n
# and counts down from n

def countdown(n):
    for i in range(n,0,-1):
        print(i)

countdown(10)

def countdown_rec(n):
    if(n <= 0):
        pass
    else:
        print(n)
        countdown_rec(n-1)

countdown_rec(10)


def concat(n):
    if(n <= 0):
        return []
    else:
        return concat(n-1) + [n]

print(concat(10))
