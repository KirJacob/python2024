def sum_pairs(ints, s):
    int_dict = {}
    for number in ints:
        int_dict[number] = number

    answers = list()

    for number in ints:

        other_list = list(ints)
        other_list.remove(number)
        print(f"number={number} other_list={other_list}")
        if other_list.__contains__(s - number):
            print(f"found={number} {s - number}")
            answers.append([number, s - number])
    if len(answers) != 0:
        return answers
    else:
        return None


print(sum_pairs([10, 5, 2, 3, 7, 5], 10))


# def test_positive():
#     assert sum_pairs([11, 3, 7, 5], 10) == [3, 7]
#     assert sum_pairs([4, 3, 2, 3, 4], 6) == [4, 2]
#     assert sum_pairs([0, 0, -2, 3], 2) is None
#     assert sum_pairs([10, 5, 2, 3, 7, 5], 10) == [3, 7]
