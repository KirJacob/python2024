def multiply(*arguments):
    print("multiply_debug=" + str(arguments[0]))
    total = 1
    for element in arguments:
        total *= element
        print(element)
    return total


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print(f"result+={apply(3, 5, operator='+')}")
print(f"result*={apply(3, 5, operator='*')}")
print(f"result*={apply(1, 2, 3, 4, operator='+')}")
print(f"result*={multiply(1, 2, 3, 4)}")

print("--------------")


def try_args(*args):
    print(*args)
    print(args)


try_args(1, 2, 3)
t01 = ((1, 1, 1), (2, 3, 4))
t02 = (1, 2, 3)
print(t01)
print(*t01)
