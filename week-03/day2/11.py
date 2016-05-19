students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]
# create a function that takes a list of students,
# then returns how many candies are own by students
# under 10


print(students[1]['name'])

for student in students:
    print(student['age'])

for student in students:
    if student['age'] < 10:
        print(student['name'])


candy = 0
for student in students:
    if student['age'] < 10:
        candy += student['candies']
print(candy)


def total_candy(input):
    candy = 0
    for i in input:
        if i['age'] < 10:
            candy += i['candies']
    return candy

print(total_candy(students))

def get_all_canies_of_under_10(student_list):
    candy = 0
    for student in student_list:
        if student['age'] < 10:
            candy += student['candies']
    return candy

print(get_all_canies_of_under_10(students))
