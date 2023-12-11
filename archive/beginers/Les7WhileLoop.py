import Les0MyHelper
# Lesson 7 While Loop

x = 0
sum_count = 0
while x < 10:
    print(x)
    sum_count += x
    x += 1
print(sum_count)

my_list = [7, 5, 4, 1, -5, -2]
total3 = 0
i3 = 0

while my_list[i3] > 0:
    total3 += my_list[i3]
    i3 += 1

total4 = 0
for number in my_list:
    if number <= 0:
        break
    else:
        total4 += number

Les0MyHelper.print_var("total3", total3)
print("total3: " + str(total3))
print("total4: " + str(total4))

my_list2 = [7, 5, 4, 1]
total5 = 0
i5 = 0

while i5 < len(my_list2) and total5 < 100 and my_list2[i5] > 0:
    total5 += my_list2[i5]
    i5 += 1

print(total5)

# endless cycle
# while 1 < 2:
#     print("Hello")

# my_list -> count all negatives with for and while
Les0MyHelper.separator()
my_list_neg = [3, 4, 4, -4, -14, -5]
# with for in
total6 = 0
for element in my_list_neg:
    if element > 0:
        total6 += element
print("total6=" + str(total6))

# with while
index = 0
total7 = 0
while index < len(my_list_neg):
    if my_list_neg[index] < 0:
        total7 += my_list_neg[index]
    index += 1
print("total7=" + str(total7))

# with while from the end
index8 = len(my_list_neg) - 1
total8 = 0
while my_list_neg[index8] < 0:
    total8 += my_list_neg[index8]
    index8 -= 1
    print("index8=" + str(index8))
print("total8=" + str(total8))

# with for in from the end
index9 = len(my_list_neg) - 1
total9 = 0
list9_rev = list(reversed(range(0, len(my_list_neg))))
print("index9_rev=" + str(list9_rev))
for element_index in list9_rev:
    if my_list_neg[element_index] < 0:
        total9 += my_list_neg[element_index]
print("total9=" + str(total9))

Les0MyHelper.separator("words")
words = ["apple", "banana", "grape", "some other word", "stop", "hello", "goodbye"]
for word in words:
    if word == "stop":
        break
    print(word)



