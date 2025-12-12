from codewars.utils.decorators import exec_time

@exec_time
def stray(arr):
    return list(filter(lambda x: len(list(filter(lambda y: y == x, arr))) == 1, set(arr)))[0]

def test_stray():
    assert stray([1, 1, 2]) == 2
    assert stray([17, 17, 3, 17, 17, 17, 17]) == 3

test_stray()
