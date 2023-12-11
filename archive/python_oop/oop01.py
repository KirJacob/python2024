class Contact:

    # static class level fields
    country = "Ukraine"
    year = 2022

    # constructor and internal field which is calculated
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.welcome = f"Hello, My name is {self.name}, I am {self.age} years old"

    def get_welcome(self):
        return f"Hello, My name is {self.name}, I am {self.age} years old"

    def get_welcome_v2(self):
        return self.welcome + f", It's year {Contact.year}, I live in {Contact.country}"


class Animal:
    def __init__(self, breed, legs, food):
        self.breed = breed
        self.legs = legs
        self.food = food

    def say_hi(self):
        print(f"Hey, i am {self.breed}, i have {self.legs} legs and i like to eat {self.food}")


class Dog(Animal):
    # calling parent constructor
    def __init__(self, breed, legs, food, master):
        super().__init__(breed, legs, food)
        self.master = master

    def bark(self):
        print(f"Dogs can bark! and has a master {self.master}")


class Shepard(Dog):
    def guard(self):
        print("Shepards are good guards")


class Cat(Animal):
    def drink_milk(self):
        print("Cats can say Meow and drink milk")

    # overriding parent method
    def say_hi(self):
        super().say_hi()
        print("Also you know cats are very clever! they are better then dogs! :-)")


dog = Dog("Dog", 4, "Meat", "Kirill")
dog.say_hi()
dog.bark()
shepard = Shepard("Dog", 4, "Meat", "Vika")
shepard.say_hi()
shepard.bark()
shepard.guard()
cat = Cat("Cat", 4, "Fish")
cat.say_hi()
cat.drink_milk()


# contact01 = Contact("Kirill", 41)
# contact02 = Contact("Vika", 36)
#
# print(contact01.get_welcome())
# print(contact02.get_welcome())
# print(contact01.welcome)
# print(contact01.get_welcome_v2())
