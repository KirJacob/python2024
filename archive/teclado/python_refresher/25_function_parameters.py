def add(x, y=1):
    result = x + y
    print(result)


add(5, 5)
add(y=4, x=3)
add(10)


def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"


divide(dividend=10, divisor=1)


# changing the value that define default parameter doesnt modify the function
# just return will return None
