students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

# create a function that counts the students that
# has more than 4 candies

def get_students_with_more_than_four_candies(student_list):
    four_candies = 0
    for student in student_list:
        if student['candies'] > 4:
            four_candies += 1
    return four_candies

print(get_students_with_more_than_four_candies(students))
