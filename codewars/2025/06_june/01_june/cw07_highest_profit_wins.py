def min_max(lst):
    return [min(list(lst)), max(list(lst))]


def test_min_max():
    assert min_max([1, 2, 3, 4, 5]) == [1, 5]
    assert min_max([2334454, 5]) == [5, 2334454]
