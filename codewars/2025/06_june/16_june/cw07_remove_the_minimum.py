def remove_smallest(numbers):
    result = []
    occurred = False
    if len(numbers) != 0:
        min_value = min(numbers)
        for number in numbers:
            if (not occurred) and number == min_value:
                occurred = True
            else:
                result.append(number)
        return result
    else:
        return []


# def test_remove_smallest():
#     assert remove_smallest([1, 2, 3, 4, 5]) == [2, 3, 4, 5]
#     assert remove_smallest([5, 3, 2, 1, 4]) == [5, 3, 2, 4]
#     assert remove_smallest([1, 2, 3, 1, 1]) == [2, 3, 1, 1]
#     assert remove_smallest([]) == []

# numbers[0:idx] + numbers[idx+1:]
numbers = [21, 3, 5, 7, 8, 10, 100]
print(numbers[0:2])
print(numbers[:3])
print(numbers[3:])

