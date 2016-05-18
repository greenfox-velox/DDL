ae = 'Jozsi'
# create a function that greets ae

def greet(name):
    return "hello, " +  name

print(greet(ae))

def test(expected, actual):
    if expected == actual:
        print("Check")
    else:
        print("Fokit")

test("hello, Jozsi", greet(ae))
