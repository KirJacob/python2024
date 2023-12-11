import Les0MyHelper
import math


class PersonOld:
    def print_info(self, n):
        for num in range(n):
            print(f"Name:{self.name}, Surname:{self.surname}, Birthplace:{self.birth_place}")


class Person:
    # class level attributes - same like static field in Java
    some_num = 10
    stat = 0

    def __init__(self, name, surname, birth_place, year_of_birth):
        self.name = name
        self.surname = surname
        self.birth_place = birth_place
        self.year_of_birth = year_of_birth
        Person.stat = Person.stat + 1

    # self parameters
    def get_age(self, current_year):
        return current_year - self.year_of_birth

    def print_info(self, n):
        for num in range(n):
            print(f"Name:{self.name}, Surname:{self.surname}, Birthplace:{self.birth_place}")


# 2nd approach for object creation
p1 = Person("Elon", "Mask", "South Africa", 1971)

# 1st approach for object creation
p2 = PersonOld()
p2.name = "Sergei"
p2.surname = "Korolev"
p2.birth_place = "Ukraine"
p2.year_of_birth = 1907

print(p1.name)
Les0MyHelper.separator()
p1.print_info(1)
Les0MyHelper.separator()
p2.print_info(2)
Les0MyHelper.separator()

# 2nd approach on calling methods
Person.print_info(p1, 1)
print(p1.get_age(2021))

# Constructors
# p3 = PersonOld()
# p3.name = "Albert"
# # wrong field name
# # p3.suname = "Einstein"
# p3.surname = "Einstein"
# p3.year_of_birth = 1879
# # we have forgotten to specify birth_place
# p3.print_info(1)

Les0MyHelper.separator()
p4 = Person("Albert", "Einstein", "Switzerland", 1879)
p4.print_info(1)

# we can add new fields
p4.test = "someTest"
print(Person.some_num)
print(p4.some_num)
p4.some_num = 1313
print(Person.some_num)
print(p1.some_num)
print(p4.some_num)

Les0MyHelper.separator("CIRCLE")
p5 = Person("Mark", "Zuckerberg", "United States", 1981)


class Circle:

    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def get_square(self):
        return Circle.PI * self.radius * self.radius

    def get_perimeter(self):
        return Circle.PI * 2 * self.radius

    def print_circle(self):
        print(f"Circle(radius={self.radius} square={self.get_square()} length={self.get_perimeter()})")


c1 = Circle(1)
c1.print_circle()
c2 = Circle(5)
c2.print_circle()
Les0MyHelper.separator()
print(Person.stat)









