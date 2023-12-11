import Les0MyHelper

names = ["Mike", "Tom", "Katy", "Alex", "Kirill"]
for element in names:
    print(element)

Les0MyHelper.separator()
for i in range(0, 4):  # 0,1,2,3
    print(names[i])

Les0MyHelper.separator()
for i in range(4):  # 0,1,2,3
    print(names[i])

Les0MyHelper.separator()
for i in range(len(names)):  # 0,1,2,3
    print(names[i])

# Nested loop
Les0MyHelper.separator()
for i in range(len(names)):
    for j in range(i + 1):
        print(names[i])
