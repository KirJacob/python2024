def get_sum(a, b):
    if a > b:
        temp = a
        a = b
        b = temp
    return sum(range(a, b + 1))
