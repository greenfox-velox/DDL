numbers = [7, 5, 8, -1, 2]
# Write a function that returns the minimal element
# in a list (your own min function)

def minimal_num(input):
        minimum = input[0]
        for item in input:
            if item < minimum:
                minimum = item
        return minimum

print(minimal_num(numbers))
