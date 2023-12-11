import re


def get_real_floor(value):
    if value < 0:
        return value + 1
    elif value == 0:
        return 1
    elif value < 13:
        return value - 1
    else:
        return value - 2


def digitize(n):
    return [int(element) for element in list(reversed(list(str(n))))]


def replace_dots(str):
    print(str)
    return re.sub(r"..", "-", str)


print(replace_dots("hello.there"))



