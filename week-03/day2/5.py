# create a function that returns it's input factorial

def fact_it(input):
    f = 1
    for i in range(1, input+1):
        f *= i
    return(f)

print(fact_it(5))
