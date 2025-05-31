def unique_in_order(sequence):
    sequence_lst = list(sequence)
    result_lst = []
    for element in sequence_lst:
        if len(result_lst) == 0:
            result_lst.append(element)
        elif result_lst[len(result_lst) - 1] != element:
            result_lst.append(element)
    return result_lst

str01 = "AAAABBBCCDAABBB"
str02 = "ABBCcAD"
lst03 = [1, 2, 2, 3, 3]
lst03 = (1, 2, 2, 3, 3)


def test_positive():
    assert unique_in_order("AAAABBBCCDAABBB") == ['A', 'B', 'C', 'D', 'A', 'B']
    assert unique_in_order("ABBCcAD") == ['A', 'B', 'C', 'c', 'A', 'D']
    assert unique_in_order([1, 2, 2, 3, 3]) == [1, 2, 3]
    assert unique_in_order((1, 2, 2, 3, 3)) == [1, 2, 3]
