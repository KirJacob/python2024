#  Inheritance  -  is-a
import Les0MyHelper


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Les0MyHelper.separator()
        print("Person created")

    def say_hello(self):
        print(f"{self.name} says hello!")


class Student(Person):
    def __init__(self, name, age, average_grade):
        # 1st option on how to call parent constructor
        # Person.__init__(self, name, age)
        super().__init__(name, age)
        self.average_grade = average_grade
        print("Student created")

    # overriding parent method
    def say_hello(self):
        super().say_hello() # calling parent class method
        print(f"Student with name {self.name} says hello!")

    def study(self):
        print(f"{self.name} studies with grade {self.average_grade}")


class Teacher(Person):
    def teach(self):
        print(f"{self.name} teaches")


def introduce(person):
    print("Now, a person will say hello!")
    person.say_hello()


p1 = Person("Elon", 40)
p1.say_hello()

s1 = Student("Mike", 18, 4.5)
s1.say_hello()
s1.study()

t1 = Teacher("Katy", 45)
t1.say_hello()
t1.teach()

Les0MyHelper.separator()
introduce(s1)

Les0MyHelper.separator()
Les0MyHelper.separator()

people_arr = [Student("Tom", 18, 3.5), Teacher("Katy", 35), Student("Bob", 26, 4.8)]
for person in people_arr:
    introduce(person)

Les0MyHelper.separator()
Les0MyHelper.separator()


class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def bark(self):
        print(f"Dog named {self.name} with breed {self.breed} is barking!")


class Cat(Animal):
    def meow(self):
        print(f"{self.name} says Meow!")


class Frog(Animal):

    def eat(self):
        print(f"Frog with name {self.name} is eating")


d1 = Dog("Tuzik", "Dvornyaga")
d2 = Dog("Pushok", "Ovcharka")
c3 = Cat("Murka")
f4 = Frog("Cermet")
f4.eat()
d1.eat()
d1.bark()
c3.meow()

tuple1 = (1,2)
tuple2 = (4,5)
print(tuple1[0])
print(tuple1[1])
print(tuple1 + tuple2)


