# Create a class called "Car"
# It should have a "type" property that stores the car's type in a string eg: "Mazda"
# It should have a "km" property that stores how many kilometers it have run
# The km and the type property should be a parmeter in the constructor
# It should have a method called "run" that takes a number and increments the "km" property by it

class Car():

    def __init__(self, type, km):
        print('Zoomzoomzoom')
        self.type = type
        self.km = km

    def ride(self, addKm):
        self.km = self.km + addKm
        return self.km


my_mazda = Car('mazda', 12000)
my_mazda.ride(100)
print(my_mazda.type)
print(my_mazda.km)
