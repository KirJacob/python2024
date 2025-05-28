import Les0MyHelper
import pytest

Les0MyHelper.separator("sortme")


# input: names - unsorted list
# output: sorted list
def sortme(names):
    for cursor in range(0, len(names) - 1):
        for index in range(0, len(names) - 1 - cursor):
            if names[index] > names[index + 1]:
                temp = names[index + 1]
                names[index + 1] = names[index]
                names[index] = temp
            print(names)
    return names


# test
# print("result=" + str(sortme([100,5,3,4,15])))
# print("result=" + str(sortme([10,5,30,4,150])))
# print("result=" + str(sortme(["one", "two", "three"])))
print("result=" + str(sorted(["one", "two", "three"])))
Les0MyHelper.separator("no_odds")


def no_odds_option1(values):
    result = []
    for num in values:
        if num % 2 == 0:
            result.append(num)
    return result


def no_odds_option1(values):
    result = []
    for num in values:
        if num % 2 == 0:
            result.append(num)
    return result


def no_odds_option2(values):
    return [num for num in values if num % 2 == 0]


print(no_odds_option1([2,1,10,7,0,3]))
print(no_odds_option2([2,1,10,7,0,3]))


Les0MyHelper.separator("high_and_low")


def high_and_low(numbers):
    list_int = [int(i) for i in numbers.split(" ")]
    return f"{max(list_int)} {min(list_int)}"


print(high_and_low("1 2 3 4 5"))  # return "5 1"
print(high_and_low("1 2 -3 4 5")) # return "5 -3"
print(high_and_low("1 9 3 4 -5")) # return "9 -5"
