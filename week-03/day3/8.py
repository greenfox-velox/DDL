# Create a new class called `Person` that has a first_name and a last_name (takes it in it's constructor)
# It should have a `greet` method that prints it's full name

# Create a `Student` class that is the child class of `Person`
# it should have a method to add grades
# it should have a `salute` method that prints it's full name and the average of it's grades as well

class Person():
    def __init__(self):
        self.first_name = first_name
        self.last_name = last_name
        return

    def greet(first_name, last_name):
        return first_name + last_name

person1 = Person
print(person1.greet("Feri ", "Vágási"))

class Student(Person):

    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 5:
            self.grades += [grade]
        return self.grades

    def average(self):
        total = 0
        for num in self.grades:
            total += num
        self.average = total/len(self.grades)
        return self.average

    def salute(self, first_name, last_name):
        return str(self.average) + first_name + last_name


feri = Student()
feri.add_grade(5)
feri.add_grade(2)
feri.add_grade(4)
feri.add_grade(3)
feri.add_grade(2)
feri.add_grade(5)
feri.average()
print(feri.salute(" Feri ", "Vágási"))
