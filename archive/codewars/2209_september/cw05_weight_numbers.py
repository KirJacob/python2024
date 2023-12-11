def weight_calculate(num_str):
    return sum(list(map(lambda digit: int(digit), list(num_str))))


def compare_weight(num1, num2):
    if weight_calculate(num1) > weight_calculate(num2):
        return True
    elif weight_calculate(num1) == weight_calculate(num2):
        return num1 > num2
    else:
        return False


def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(0, len(lst) - 1 - i):
            if compare_weight(lst[j], lst[j + 1]):
                temp = lst[j]
                lst[j] = lst[j + 1]
                lst[j + 1] = temp
    return lst


def order_weight(strng):
    lst = strng.split(" ")
    return " ".join(bubble_sort(lst))


expected = "11 11 2000 10003 22 123 1234000 44444444 9999"
tst_str = "2000 11 11 10003 22 123 1234000 44444444 9999"
print(order_weight(tst_str))


print(f"{'22' > '10003'}")

print(f"compare_weight={compare_weight('22', '10003')}")



