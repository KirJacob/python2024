# too expensive solution
# def find_uniq(arr):
#     return list(filter(lambda x: len(list(filter(lambda y: x == y, arr))) == 1, arr))[0]


def find_uniq(arr):
    set_arr = set(arr)
    for num in set_arr:
        if len(list(filter(lambda x: num == x, arr))) == 1:
            return num


def test_positive():
    assert find_uniq([1, 1, 1, 2, 1, 1]) == 2
    assert find_uniq([0, 0, 0.55, 0, 0]) == 0.55
