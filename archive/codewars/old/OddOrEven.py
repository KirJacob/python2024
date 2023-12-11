def odd_or_even(arr):
    if len(arr) == 0:
        return [0]
    elif sum(arr) % 2 == 0:
        return "even"
    else:
        return "odd"


lst01 = [1, 2, 4, 5]
lst02 = []
print(odd_or_even(lst01))
print(odd_or_even(lst02))


def oddOrEven2(arr):
    return 'even' if sum(arr) % 2 == 0 else 'odd'

# for comprehension


print(0 if 2 % 2 == 0 else 1)
