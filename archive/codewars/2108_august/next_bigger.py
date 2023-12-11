def join_int_list(lst):
    return int("".join([str(num) for num in lst]))


def next_big_int(num_compare, list_num):
    list_num.sort()
    for num_list in list_num:
        if num_list > num_compare:
            return num_list


def next_bigger(n):
    lst_num = [int(digit) for digit in list(str(n))]
    lst_copy = lst_num.copy()
    lst_copy.sort(reverse=True)
    first_occ = True
    if lst_copy == lst_num:
        return -1
    for index in range(len(lst_num) - 1, -1, -1):
        if lst_num[index] > lst_num[index - 1]:
            if first_occ:
                lst_num[index - 1], lst_num[index] = lst_num[index], lst_num[index - 1]
                return join_int_list(lst_num)
            else:
                list_left = lst_num[0:index - 1]
                list_exclude = lst_num[index-1:len(lst_num)]
                to_replace = next_big_int(lst_num[index - 1], lst_num[index:len(lst_num)])
                list_exclude.remove(to_replace)
                list_exclude.sort()
                list_left.append(to_replace)
                list_res = list_left + list_exclude
                return join_int_list(list_res)
        else:
            first_occ = False

    return -1


# print(next_bigger(12543))
# print(next_bigger(1543))
# print(next_bigger(12)) #21
# print(next_bigger(513)) #531
# print(next_bigger(2017)) #2071
# print(next_bigger(414)) #441
# print(next_bigger(144)) #414
# print(next_bigger(321)) # -1
#
# print(next_bigger(132)) #213
# print(next_bigger(1543)) # 3145
# print(next_bigger(11543)) # 13145
# print(next_bigger(1234567890)) #1234567908
# print(next_bigger(1234567890)) #1234567908


# 12345 - 12354
# 12354 - 12435
# 12435 - 12453

#  APPROACH
#  CASE-1
#  if sorted desc then -1, 3210

# 1234567089 should equal 1234567908
# print(next_bigger(1234567890)) # 1234567089
# print(next_bigger(1234567891)) # 1234567089
# 1234567891
#
# print(next_bigger(123)) # 132 -     OK
# print(next_bigger(1234)) # 1243 -   OK
# print(next_bigger(321)) # -1 -      OK
# print(next_bigger(3210)) # -1 -     OK
# print(next_bigger(1543)) # -3145    OK

lst_test1 = [1,1,2,3]
lst_test1.remove(1)
print(lst_test1)
print(next_big_int(3, [6, 5, 2]))
print(next_bigger(134652))  # -135246 -     NO


