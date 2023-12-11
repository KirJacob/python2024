import math


def digit_hex_to_num(hex_digit):
    code = ord(hex_digit.lower())
    if 47 < code < 58:
        return code - 48
    elif 96 < code < 103:
        return code - 87
    else:
        return "Cannot convert to hex digit"


def hex_string_to_decimal(hex_string):
    list_hex = list(hex_string)
    size = len(list_hex) - 1
    result = 0
    for num in range(size, -1, -1):
        result = result + math.pow(16, num) * digit_hex_to_num(list_hex[size - num])
    return int(result)


def hex_string_to_RGB(hex_string):
    res = dict()
    res["r"] = hex_string_to_decimal(hex_string[1:3])
    res['g'] = hex_string_to_decimal(hex_string[3:5])
    res['b'] = hex_string_to_decimal(hex_string[5:7])
    return res


print(ord("a"))
print(ord("A".lower()))
print(ord("1".lower()))

digit_hex_to_num("a")
letters = ["a", "b", "c", "d", "e", "f"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for letter in letters:
    print(f"letter={digit_hex_to_num(letter)}")
for digit in digits:
    print(f"digit={digit_hex_to_num(digit)}")
for num in range(3, -1, -1):
    print(num)

print(hex_string_to_RGB("#FF9933"))
lst = list([1,11,2,3])
lst.pop(0)
print(lst)
print(hex_string_to_RGB("#FF9933"))
