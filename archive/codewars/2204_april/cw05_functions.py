def plus(arg):
    return "+", arg


def minus(arg):
    return "-", arg


def times(arg):
    return "*", arg


def divided_by(arg):
    return "/", arg


def zero(*args):
    return common_fun(args, 0)


def one(*args):
    return common_fun(args, 1)


def two(*args):
    return common_fun(args, 2)


def three(*args):
    return common_fun(args, 3)


def four(*args):
    return common_fun(args, 4)


def five(*args):
    return common_fun(args, 5)


def six(*args):
    return common_fun(args, 6)


def seven(*args):
    return common_fun(args, 7)


def eight(*args):
    return common_fun(args, 8)


def nine(*args):
    return common_fun(args, 9)


def operator(operator_char, param1, param2):
    if operator_char == '+':
        return param1 + param2
    elif operator_char == '-':
        return param1 - param2
    elif operator_char == '*':
        return param1 * param2
    elif operator_char == '/':
        return int(param1 / param2)
    else:
        return Exception("operator is not recognized")


def common_fun(args, number):
    number_args = len(args)
    if number_args == 0:
        return number
    elif number_args == 1:
        return operator(args[0][0], number, args[0][1])


print(f"res={two()}")
print(f"res={zero()}")
print(f"res={four(divided_by(two()))}")



