# ISBN     : 1 1 1 2 2 2 3 3 3  9
# position : 1 2 3 4 5 6 7 8 9 10
# (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

import re

def valid_ISBN10(isbn):
    def convert_digit(digit):
        if digit=='X':
            return 10
        else:
            return int(digit)
    list_isbn = list(isbn)
    # validate digits
    for digit_num in range(0, len(list_isbn)):
        if list_isbn[digit_num] == "X" and digit_num != 9:
            return False
        if len(re.findall("\\d|X", list_isbn[digit_num])) == 0:
            return False
    list_isbn_int = [convert_digit(list_isbn[num]) * (num + 1) for num in range(0, len(list_isbn))]
    if len(list_isbn) != 10:
        return False
    else:
        return sum(list_isbn_int) % 11 == 0


print(valid_ISBN10("X123456788"))
