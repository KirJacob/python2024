import math


def last_n(n):
    lst = list(str(n))
    last = int(lst[len(lst) - 1])
    return last


def last_digit(n1, n2):
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


print(last_digit(3, 3))
print(2**10)

# 1 - 1
# 0 - 0
# 2 - 2,4,8,6,2,4,8,6,2 ../1/5/9
# 3 - 3,9,7,1,3 ..
# 4 - 4,6,4
# 5 - 5,5,5
# 6 - 6,6
# 7 - 7,9,3,1,7
# 8 - 8,4,2,6,8
# 9 - 9,1,9
