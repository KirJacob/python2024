import Les0MyHelper

# Sets
# sets
set01 = {13, 1, 34, 7}
set02 = {1, 2, 21, 4}
print(set01)
print(set01.union(set02))

# for sets in result is given immediately
a = set()
print(a)  # empty set
b = set([1, 23, 4, 5])
print(b)
c = {2, 23, 1}
print(c)
c.add(5)
print(c)
c.add(5)
c.add("hello")
print(c)

for e in b:
    print(e)

my_list = [1, 2, 1, 1, 5, "hello", "hello"]

# Removing duplicates - option1
my_set = set()
for e in my_list:
    my_set.add(e)
print(my_set)

# Removing duplicates - option2 - convert list to set
my_set2 = set(my_list)
print(my_set2)

# convert set to list back
my_list2 = list(my_set2)
print(my_list2)

# verifying is element in set using "in"
a = {"hello", "hey", 1, 2}
print(5 in a)
print("hey" in a)
print(5 not in a)  # not

my_list3 = [1, 2, 3]
my_set3 = {1, 2, 3}
print(my_list3[0])
# print(my_set3[0]) this will throw exception

# Task 1 - count sum of unique elements in set
my_list4 = [1, 1, 2, 5, 10, 10, 10]
my_set4 = set(my_list4)
sum_set4 = sum(my_set4)
print(sum_set4)


# Task 2 - set, list -> if all elements from set are in the list
def check_set_in_list(set_arg, list_arg):
    for e in set_arg:
        if e not in list_arg:
            return False
    return True


set5 = {1, 2, 3}
set6 = {1, 2, 6}
list5 = [1, 2, 3, 5]
print(check_set_in_list(set5, list5))
print(check_set_in_list(set6, list5))


# Task 2 - set, list -> if all elements from set are in the list
def check_list_in_set(set_arg, list_arg):
    if len(set_arg) > len(list_arg):
        return False
    else:
        for element in set(list_arg):
            if element not in set_arg:
                return False
        return True


Les0MyHelper.separator("task2")
set7 = {1, 3}
set8 = {1, 2, 6}
list7 = [1, 2, 1]
print(check_list_in_set(set7, list7))
print(check_list_in_set(set8, list7))
print(check_list_in_set({1, 2}, [3]))
print(check_list_in_set({1, 2, 3, 4, 5}, [2, 3, 10]))
