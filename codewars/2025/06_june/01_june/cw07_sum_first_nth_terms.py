def series_sum(n):
    result = 1.00
    for index in range(1, n):
        result = result + 1 / (3 * index + 1)
    if n == 0:
        return "0.00"
    else:
        return f"{result:.2f}"


def test_series_sum():
    assert series_sum(1) == "1.00"
    assert series_sum(2) == "1.25"
    assert series_sum(3) == "1.39"
