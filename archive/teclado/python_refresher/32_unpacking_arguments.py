def multiply(*arguments):
    total = 1
    for element in arguments:
        total *= element
    return total


# last argument should be operator named
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"


print("res*=" + str(apply(3, 5, operator="*")))
print("res+=" + str(apply(3, 5, operator="+")))
print("res==" + apply(3, 5, operator="="))
# print(f"apply_res={apply(1, 2, operator = lambda x, y: x + y)}")

multiply(1, 2, 34)
print(multiply(1, 2, 34))
print(multiply(1, 3, 5))


def add(x, y):
    return x + y


# ONE STAR unpacking arguments from a list
nums = [3, 5]
print(add(*nums))

print(add(x=5, y=8))

nums_dict = {"x": 15, "y": 25}
print(add(nums_dict["x"], nums_dict["y"]))
print(add(x=nums_dict["x"], y=nums_dict["y"]))

# TWO STARS passing named arguments (dictionary of arguments)
print(add(**nums_dict))
