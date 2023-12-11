class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # same as toString in Java
    def __str__(self):
        return f"Hello, my name is {self.name}, i am {self.age} years old"

    # is printed when there is no __str__ method, smth like hash method
    def __repr__(self):
        return f"<Person({self.name},{self.age})>"


kirill = Person("Kirill", 41)
bob = Person("Bob", 35)
print(bob)

dict1 = {'name': 'kirill', "age": 41}
dict2 = {'name': 'vika', "age": 36}
list0 = [dict1, dict2]
res = sum(list(map(lambda x: x['age'], list0)))
print(res)
