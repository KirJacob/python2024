def score(dice):
    total = 0
    dict_num = {n: dice.count(n) for n in [6, 5, 4, 3, 2, 1]}

    if dict_num[1] >= 3:
        inc = 1000 + 100 * (dict_num[1] - 3)
        print(f"inc={inc} for three 1's and more")
        total = total + inc
    else:
        inc = 100 * dict_num[1]
        print(f"inc={inc} for 1's")
        total = total + inc

    if dict_num[5] >= 3:
        inc = 500 + 50 * (dict_num[5] - 3)
        print(f"inc={inc} for three 5's and more")
        total = total + inc
    else:
        inc = 50 * dict_num[5]
        print(f"inc={inc} for 5's")
        total = total + inc

    for num in [6, 4, 3, 2]:
        if dict_num[num] >= 3:
            inc = 100 * num
            print(f"inc={inc} for three {num}'s")
            total = total + inc

    return total


# dice = [1, 1, 4, 5, 3]
# print(score(dice))

# 300 should equal 400
dice = [4, 4, 4, 3, 3]
print(score(dice))

# 350 should equal 450
dice = [2, 4, 4, 5, 4]
print(score(dice))
