import math


def last_n(n):
    lst = list(str(n))
    last = int(lst[len(lst) - 1])
    return last


def last_single_digit(n1, n2):
    if n2 == 0:
        return 1
    last_num = last_n(n1)
    if last_num in {0, 1, 5, 6}:
        return last_num
    elif last_num in {4, 9}:
        if n2 % 2 == 0:
            if last_num == 4:
                return 6
            elif last_num == 9:
                return 1
        else:
            return last_num
    elif last_num in {2, 3, 7, 8}:
        if n2 % 4 != 0:
            return last_n(int(math.pow(last_num, n2 % 4)))
        else:
            return last_n(int(math.pow(last_num, 4)))


def last_digit(lst):
    for num in range(len(lst) - 1, - 1, -1):
        print(f"num={num} {lst[num]}")
    # Your Code Here
    pass


test_data = [
    ([], 1),
    ([0, 0], 1),
    ([0, 0, 0], 0),
    ([1, 2], 1),
    ([3, 4, 5], 1),
    ([4, 3, 6], 4),
    ([7, 6, 21], 1),
    ([12, 30, 21], 6),
    ([2, 2, 2, 0], 4),
    ([937640, 767456, 981242], 0),
    ([123232, 694022, 140249], 6),
    ([499942, 898102, 846073], 6)
]

last_digit([12, 30, 21])