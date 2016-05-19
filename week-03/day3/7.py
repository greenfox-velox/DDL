# create a function that takes a list and returns a new list with all the elements doubled

easy_list = [1,2,3,4,5,6,7,8,9]

def double_list(input_list):
    double = []
    for item in input_list:
        item = item * 2
        double += [item]
    return(double)

print(double_list(easy_list))
