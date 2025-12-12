# enumerate names with number
lst_name = ["Bob", "John", "Elizabeth"]
for element in enumerate(lst_name):
    print(element)

# zip lists in one
lst_01 = ["Paris", "London", "Berlin"]
lst_02 = ["France", "UK", "Germany"]
print(list(zip(lst_01, lst_02)))

# slicing
lst = [0,1,2,3,4,5,6,7,8,9]
print(f"[3:7]={lst[3:7]}")  #[3, 4, 5, 6]
print(f"[:3]={lst[:3]}")  #[0, 1, 2]
print(f"[3:]={lst[3:]}")  #[3, 4, 5, 6, 7, 8, 9]
print(f"[::-1]={lst[::-1]}")  #[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(f"[::2]={lst[::2]}")  #[0, 2, 4, 6, 8]

# list extend
lst_ext = [1, 2, 3]
lst_ext.extend([4, 5, 6])
print(lst_ext)

# generators
def counter():
    for i in range(3):
        yield i

g = counter()
print(next(g))  # 0
print(next(g))  # 1
print(next(g))  # 2

h = (x*x for x in range(50))
print(next(h))  # 0
print(next(h))  # 1
print(next(h))  # 4

# unpacking
a, b, c = [1,2,3]
