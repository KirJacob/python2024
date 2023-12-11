import Les0MyHelper

a = [1, 2, 3, 4, 5]

# without list comprehension
b = []
for element in a:
    b.append(element * 2)
print(b)

# List Comprehension
c = [num * 2 for num in a]
print(c)

# 'even' if sum(arr) % 2 == 0 else 'odd'
range3 = [num * 3 for num in range(1, 6)]
print(range3)

range3old = []
for num in range(1, 6):
    range3old.append(num * 3)
print(range3old)

# filtering values
ea = [1, 10, 12, 4, 3, 20, 55]
a_filter = []
for num in ea:
    if num < 10:
        a_filter.append(num)
print(a_filter)

a_filtered = [num for num in ea if num < 10]
a_filtered_squared = [num * num for num in ea if num < 10]
print(a_filtered)
print(a_filtered_squared)

words = ["hello", "hey", "goodbye", "guitar", "piano"]
a_words = [word for word in words if len(word) < 6]
print(a_words)

# Task 1
# [20, 16, 8, 4]
# 10 - 2

Les0MyHelper.separator()
for num in range(10, 1, -1):
    print(num)

resTask01 = [num * 2 for num in range(10, 1, -1) if num % 2 == 0]
print(resTask01)

resTask02 = [word + "." for word in words if len(word) > 5]
print(resTask02)
