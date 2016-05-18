numbers = [3, 4, 5, 6, 7]
# write a function that reverses a list

def reverser(input):
    reverse = []
    for i in range(len(input) -1, -1, -1):
        reverse += [input[i]]
    return (reverse)

print(reverser(numbers))
