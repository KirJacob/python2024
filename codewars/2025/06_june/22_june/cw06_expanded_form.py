import math


def expanded_form(num):
    num_list = list(str(num))
    length = len(num_list)
    calculated = list(map(lambda x: str(int(int(num_list[x]) * math.pow(10, length - x - 1))), range(length)))
    filtered = list(filter(lambda y: int(y) != 0, calculated))
    result = " + ".join(filtered)
    return result
