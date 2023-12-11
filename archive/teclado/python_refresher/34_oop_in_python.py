student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}


def average(sequence):
    return sum(sequence) / len(sequence)


print(average(student['grades']))
# target look - print(student.average())


class Student:

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average(self):
        result = sum(self.grades) / len(self.grades)
        return f"{result:.2f}"


student02 = Student("Rolf", (80, 90, 56))
student03 = Student("Bob", (100, 85, 93, 89))

print(student02.name)
print(student02.grades)
print(Student.average(student02))
print(student02.average())
print(student03.average())
