# Create a `Stack` class that stores elements
# It should have a `size` method that returns number of elements it has
# It should have a `push` method that adds an element to the stack
# It should have a `pop` method that returns the last element form the stack and also deletes it from it

# please don`t use the built in methods

class Kalmanka:

    def __init__(self):
        self.elements = []

    def kalman(self):
        e = 0
        for x in self.elements:
            e += 1
        return e

    def pushy(self, add):
        self.elements += [add]

    def pop(self):
        popper = self.elements[-1]
        self.elements = self.elements[0:-1]
        return popper


stack1 = Kalmanka()

stack1.pushy(1)
stack1.pushy(2)
stack1.pushy(3)
stack1.pushy(4)
stack1.pushy(5)
stack1.pushy(6)
stack1.pushy(8)
print(stack1.kalman())
print(stack1.elements)
print(stack1.pop())
print(stack1.elements)
