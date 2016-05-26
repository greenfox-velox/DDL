# 2. write a recursive function
# that takes one parameter: n
# and adds numbers from 1 to n

def sumi(n):
    if(n <= 0):
        return 0
    else:
        return n + sumi(n-1)

print(sumi(10))


def sumi2(n):
    if(n <= 0):
        return 0
    else:
        return sumi2(n-1) + n

print(sumi2(10))
