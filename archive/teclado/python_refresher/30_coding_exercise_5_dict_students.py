def average_grade(data):
    grades = data['grades']
    return sum(grades)/len(grades)


def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total += sum((student['grades']))
        count = count + len(student['grades'])
    return total / count


some_student = {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)}
some_list = [
    {"name": "Jose", "school": "Computing", "grades": (66, 77, 88)},
    {"name": "Kirill", "school": "Computing", "grades": (100, 97, 98)},
    {"name": "Vika", "school": "Computing", "grades": (56, 57, 68)}
]

print(average_grade_all_students(some_list))
