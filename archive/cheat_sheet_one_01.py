# 01 - Shallow copy
numbers = [2, 3, 4, 5, 11]
numbers_copy = numbers[:]
numbers_copy[0] = 99
print(f"init list -> {numbers}, changed copy={numbers_copy}")

# 02 - Part of a list
print(numbers[0:2])
print(numbers[:3])
print(numbers[3:])

# 03 - Input and String Format
some_phrase = "Calm down {} and write your code"
name = str(input("Enter your name: "))
formatted_message = some_phrase.format(name)
print(formatted_message)

other_message = f"Hello there {name}"
print(other_message)

# 04 - Lists, Tuples, Sets
l = ["Bob", "Rolf", "Anne"]  # can remove and add, order is kept
t = ("Bob", "Rolf", "Anne")  # cannot remove or add elements in tuple, order is kept
s = {"Bob", "Rolf", "Anne"}  # element is unique, order is not guaranteed
# advanced set operations - intersect, union, difference
# list operations - append, pop

# 05 - is and == operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
res = x is y  # False
res = x is z  # True
res = x == y  # True
print(res)

# 06 - destructing tuple and list
person = ("Bob", 42, "Mechanic")
name, _, profession = person

head, *tail = [1, 2, 3, 4, 5]
print(head, tail)


# 07 - named arguments
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


divide(dividend=10, divisor=1)

# 08 - lambda functions
add = lambda x, y: x + y
multiply = lambda x, y: x * y


def calculate(func01, x, y):
    return func01(x, y)

# 09 - cannot change tuples
tuple01 = (1, 2)
# tuple01[1] = 3

