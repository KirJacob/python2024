def valid_parentheses(string):
    sum_value = 0
    for elem in list(string):
        num = 0
        if elem == ')':
            num = -1
        elif elem == '(':
            num = 1
        sum_value = sum_value + num
        if sum_value < 0:
            return False
    if sum_value == 0:
        return True
    else:
        return False


print(valid_parentheses(")()(()))"))
print(valid_parentheses("(())()"))
# -1
# 1 - 1
