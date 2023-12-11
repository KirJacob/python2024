class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


obj1 = Person
obj2 = Animal


def define_class(object):
    print(f"class={object.__name__}")


print(define_class(obj1))
print(define_class(obj2))

friend_ages = {"Rolf": 24, "Kirill": 41, "Adam": 35}
print(friend_ages["Rolf"])
friends_dict = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 21},
    {"name": "Anne", "age": 19},
]

for person in friend_ages:
    print(f"{person} {friend_ages[person]}")

for name, age in friend_ages.items():
    print(f"name={name} age={age}")
