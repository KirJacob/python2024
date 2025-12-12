import math

# endless included list
a = [1, 2, 3, 4]
a.append(a)
print(a)

# negative list index
b = [1, 2, 3, 4, 5]
print(b[1:], b[:3], b[2:3], b[::2], b[2::])

try:
    print(b[-1], b[-2])
    # print(b[-1], b[-2], b[-100])
except IndexError:
    print("too much index")


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Car brand: {self.brand}, model: {self.model}"


print(dir(Car))

def my_fun(a, b, *args):
    print(a, b, args)

my_fun(1, 2, 3, 4, 5)

def my_fun(a, b, **kwargs):
    print(a, b, kwargs)

my_fun(1, 2, x=3, y=4, z=5)

def some_func_one(z=100):
    x_param = 10
    y_param = 20
    print(locals())
    print(globals())

car01 = Car("Toyota", "Corolla")
print(car01.display_info())
# dict attribute of an object
print(car01.__dict__)
print(car01.__dict__["brand"])


