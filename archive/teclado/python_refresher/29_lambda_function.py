from my_package_kirill import some_magic

def add(x, y):
    return x + y


print(add(2, 3))

add = lambda x, y: x + y
multiply = lambda x, y: x * y


def calculate(func01, x, y):
    return func01(x, y)


print(calculate(add, 1, 2))
print(calculate(multiply, 1, 2))
print(calculate(lambda x, y: x + y, 1, 2))
print((lambda x, y: x + y)(5, 7))


def double(x):
    return x * 2


sequence = [1, 2, 3, 5, 9]
doubled = [double(x) for x in sequence]
doubled = [lambda x: x * 2 for x in sequence]
doubled = map(double, sequence)
doubled = map(lambda x: x * 2, sequence)

some_magic.some_magic()
