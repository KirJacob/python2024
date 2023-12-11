a = [3, 5, 20]
print(a)
a.append(6)
print(a)
a.append("hi")
print(a)
a.append([5, 6])  # added new element to list
print(a)
a.pop(0)  # removed element with 0 - index
print(a)
a.pop()  # removed last element
print(a)
print(a[0])  # print first element of the list
print(a[-1])  # print last element of the list
a[0] = 100  # reassigning new value to 0-s element
print(a)
a.pop(2)
print(a)

b = ["hello", "goodbye", "hey"]
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
b[0], b[2] = b[2], b[0]  # cool, replacement syntax
print(b)
