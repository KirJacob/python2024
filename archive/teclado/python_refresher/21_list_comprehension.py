
numbers = [1, 3, 5, 4, 12]
doubled = []

for num in numbers:
    doubled.append(num * 2)

compr = [num * 2 for num in numbers if num % 2 == 0]
print(compr)
print(compr is num)

print("numbers=", id(numbers), "compr=", id(compr))
