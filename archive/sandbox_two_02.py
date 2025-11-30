class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age


p1 = Person("Alex", 23)
p2 = Person("Sergey", 33)
p3 = Person("Sergey", 33)


print(p2 == p3)
