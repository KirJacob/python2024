# 01 - types and variables
class Person:
    def __init__(self, name):
        self.name = name


var01 = "Kirill"
var02 = 44
var03 = True
var04 = 1.3
var05 = [1, 2, 3]
var06 = {1, 2, 3}
var07 = {"1": 1, "2": 2}
var08 = (1, 2, 3)

all_types = [
    ("Kirill", "Mikhail"),
    (44, 45),
    (True, False),
    (1.3, 1.8),
    ([1, 2, 3], [1]),
    ({1, 2, 3}, {1}),
    ({"1": 1, "2": 2}, {"3": 3}),
    ((1, 2, 3), (1, 2)),
    (lambda x: x + 1, lambda y: y + 1),
    (None, None),
    (range(0, 10), range(0, 5)),
    (1 + 2j, -1 - 3j),
    (Person("Kirill"), Person("Mikhail"))
]

def print_value_and_type(lst):
    print(f"overall for now i know {len(lst)}-th types")
    for index in range(0, len(lst)):
        print(f"value={lst[index][0]}, type={type(lst[index][0])}")

all_types_immutable = [
    ("Kirill", "Mikhail"),
    (44, 45),
    (True, False),
    (1.3, 1.8)
]

def verify_immutable(lst):
    print(f"verifying if variable is immutable")
    for index in range(0, len(lst)):
        temp = lst[index][0]
        first_id = id(temp)
        temp = lst[index][1]
        second_id = id(temp)
        print(f"first_value={lst[index][0]} second_value={lst[index][1]} "
              f"first_id={first_id} second_id={second_id} diff_id={second_id==first_id}")


print_value_and_type(all_types)
print("\n-------------")
verify_immutable(all_types_immutable)
print("\n-------------")

# mutable
lst_m01 = [1, 2, 3]
print(f"value={lst_m01} id={id(lst_m01)}")
lst_m01[1] = 4
print(f"value={lst_m01} id={id(lst_m01)}")
print("\n-------------")

tup01 = (0, 1, 2)
# tup01[1] = 2
# TypeError: 'tuple' object does not support item assignment

print("\n-------------")
set01 = {0, 1, 2}
print(f"value={set01} id={id(set01)}")
set01.add(10)
set01.remove(2)
print(f"value={set01} id={id(set01)}")
print(set01)
# set01[1] = 2
# TypeError: 'set' object does not support item assignment

print("\n-------------")
dict = {0: "city0", 1: "city1"}
print(dict)
print(f"value={set01} id={id(set01)}")
dict[1] = "Kyiv"
print(dict)
print(f"value={set01} id={id(set01)}")

print("\n-------------")
print("\n--IS and \"==\" -----------")
x = [1, 2, 3]
y = [1, 2, 3]
print(f"x is y = {x is y}")
print(f"x==y = {x==y}")

# default list parameter is created once when function is declared, so its better to set it None

def add_item(item, lst=[]):
    lst.append(item)
    return lst
