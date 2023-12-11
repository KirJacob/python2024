import unittest
import pytest


def join_int_list(lst):
    return int("".join([str(num) for num in lst]))


def next_small_int(num_compare, list_num):
    list_num.sort(reverse=True)
    for num_list in list_num:
        if num_list < num_compare:
            return num_list


def next_smaller(n):
    lst_num = [int(digit) for digit in list(str(n))]
    lst_copy = lst_num.copy()
    lst_copy.sort()
    first_occ = True
    if lst_copy == lst_num:
        return -1
    for index in range(len(lst_num) - 1, -1, -1):
        if lst_num[index] < lst_num[index - 1]:
            if first_occ:
                lst_num[index - 1], lst_num[index] = lst_num[index], lst_num[index - 1]
                return join_int_list(lst_num)
            else:
                list_left = lst_num[0:index - 1]
                list_exclude = lst_num[index-1:len(lst_num)]
                to_replace = next_small_int(lst_num[index - 1], lst_num[index:len(lst_num)])
                list_exclude.remove(to_replace)
                list_exclude.sort(reverse=True)
                list_left.append(to_replace)
                list_res = list_left + list_exclude
                if list_res[0] == 0:
                    return -1
                return join_int_list(list_res)
        else:
            first_occ = False
    return -1


# assert next_smaller(135) == -1
# assert next_smaller(123456789) == -1
# assert next_smaller(531) == 513
# assert next_smaller(2071) == 2017
# assert next_smaller(123456798) == 123456789
# assert next_smaller(414) == 144
# assert next_smaller(7908) == 7890
# assert next_smaller(1234567908) == 1234567890
# assert next_smaller(907) == 790
# assert next_smaller(431256) == 426531

print(next_smaller(1027))


