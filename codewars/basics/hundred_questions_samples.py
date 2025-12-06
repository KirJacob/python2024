# endless included list
a = [1, 2, 3, 4]
a.append(a)
print(a)

# negative list index
b = [1, 2, 3, 4, 5]
try:
    print(b[-1], b[-2])
    # print(b[-1], b[-2], b[-100])
except IndexError:
    print("too much index")