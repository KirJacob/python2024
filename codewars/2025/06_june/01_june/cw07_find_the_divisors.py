def divisors(integer):
    result = []
    for i in range(2, int(integer/2) + 1):
        if (integer % i) == 0:
            result.append(i)
    if len(result) > 0:
        return result
    else:
        return f"{integer} is prime"


def test_divisors():
    assert divisors(15) == [3, 5]
    assert divisors(253) == [11,23]
    assert divisors(24) == [2, 3, 4, 6, 8, 12]
    assert divisors(13) == "13 is prime"
