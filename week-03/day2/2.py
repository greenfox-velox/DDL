af = 123
# create a function that doubles it's input
# double af with it

def double_it(input):
    return (2 * input)

print(double_it(af))

def test(actual, expected):
    if expected == actual:
        print('Check')
    else:
        print(':(')

test(246, double_it(af))
