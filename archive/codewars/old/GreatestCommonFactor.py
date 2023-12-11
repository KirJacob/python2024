def all_factors(num):
    result = list(i for i in range(1, int(num / 2) + 1) if num % i == 0)
    result.append(num)
    return result


def greatest_common_factor(seq):
    min_number = min(seq)
    factors = all_factors(min_number)
    max_factor = 1
    for factor in factors:
        flag_all = True
        for number in seq:
            if number % factor != 0:
                flag_all = False
        if flag_all:
            max_factor = factor
    return max_factor


print(greatest_common_factor([46, 14, 20, 88]))
print(greatest_common_factor([468, 156, 806, 312, 442]))
# 2
print(all_factors(20))
