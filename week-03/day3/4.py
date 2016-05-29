# Create a student Class
# that has a method `add_grade`, that takes a grade from 1 to 5
# an other method `get_average`, that returns the average of the
# grades

class Student():

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
        return total / len(self.grades)

bela = Student()
bela.add_grade(5)
bela.add_grade(2)
bela.add_grade(3)
bela.add_grade(4)
bela.add_grade(2)
print(bela.add_grade(5))
print(bela.average())
