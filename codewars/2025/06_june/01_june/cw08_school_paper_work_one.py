def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    else:
        return 0


def test_result_test():
    assert paperwork(5, 5) == 25
    assert paperwork(1, 2) == 2
    assert paperwork(-5, -5) == 0
