from codewars.utils.decorators import exec_time

@exec_time
def two_sum(numbers, target):
    for index_first in range(0, len(numbers)):
        for index_second in range(index_first + 1, len(numbers)):
            if numbers[index_first] + numbers[index_second] == target:
                return index_first, index_second

def test_two_sum():
    assert two_sum([1 ,2, 3], 4) == (0,2)
    assert two_sum([1234,5678,9012], 14690) == (1,2)
    assert two_sum([2, 2, 3], 4) == (0,1)


print(two_sum([3,4,5,6,7,8], 14))