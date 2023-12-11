def move_zeros(array):
    list_cleaned = list(filter(lambda x: x != 0, array))
    for i in range(0, array.count(0)):
        list_cleaned.append(0)
    return list_cleaned


print(move_zeros([1, 0, 0, 1, 2, 0, 1, 3]))
