# create a function that takes a number and divides ten with it and prints the result
# it should print "fail" if it is divided by 0

def divide_ten(number):
    value = 10

    try:
        result = 10 // number
        return result
    except ZeroDivisionError:
        return 'fail'

print(divide_ten(0))
print(divide_ten(10))
print(divide_ten(9))
print(divide_ten(8))
print(divide_ten(7))
print(divide_ten(6))
print(divide_ten(5))
print(divide_ten(4))
print(divide_ten(3))
print(divide_ten(2))
print(divide_ten(1))
