# Create a `Circle` class that takes it's radius as cinstructor parameter
# It should have a `get_circumference` method that returns it's circumference
# It should have a `get_area` method that returns it's arenit__(self, arg)

class Circle():

    def __init__(self, radius):
        print("Hello")
        self.radius = radius

    def get_circumference(self):
        circumference = 2 * self.radius * 3.14
        return circumference

    def get_area(self):
        area = self. radius **2 * 3.14
        return area

circleA = Circle(20)
print(circleA.get_circumference())
print(circleA.get_area())
