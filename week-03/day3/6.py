# create a function that takes a list and returns a new list that is reversed

easy_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

def list_reverser(input):
    reversed_list = input[::-1]
    return reversed_list

print(list_reverser(easy_list))
