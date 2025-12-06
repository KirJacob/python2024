from codewars.decorators_file import my_decorator


def paperwork(n, m):
    if n > 0 and m > 0:
        return n * m
    else:
        return 0

@my_decorator
def test_result_test():
    print(f"\n{paperwork(1, 5)}")
    print(f"\n{paperwork(1, -1)}")
    pass