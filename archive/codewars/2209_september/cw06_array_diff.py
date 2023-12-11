# array_diff([1,2,2,2,3],[2]) == [1,3]
# array_diff([1,2],[1]) == [2]

def array_diff(a, b):
    return list(filter(lambda element: not(element in b), a))


print(array_diff([1, 2, 2, 2, 3], [2]))
