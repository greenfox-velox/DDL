numbers = [4, 5, 6, 7, 8, 9, 10]
# write your own sum function

def sum_mastr(input):
    sum_of = 0
    for i in range(0, len(input)):
        sum_of += input[i]
    return(sum_of)

print(sum_mastr(numbers))
