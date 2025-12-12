import copy

a1 = [1, 2, 3]
a2 = [1, 2, 3]
b = "string"
c = "string"
print(f"b is c -> {b is c}")
print(f"b == c -> {b == c}")
print(f"a1 is a2 -> {a1 is a2}")
print(f"a1 == a2 -> {a1 == a2}")
b1 = copy.copy(a1)  # copies and detach the list
a1.append(4)
print(f"a1={a1}")
print(f"b1={b1}")
d1 = [1, 2, [3, 4], {1, 2}, (1, 2)]
d2 = copy.deepcopy(d1)  # copies and detach the list and all nested objects
d1[2].append(5)
d1[3].add(3)
print(f"d1={d1}")
print(f"d2={d2}")

def some_method(*args):
    for arg in args: print(f"arg={arg}")
    some_method(1, "string", [1, 2, 3], {"key": "value"})

def some_method_kwargs(**kwargs):
    for key, value in kwargs.items(): print(f"key={key}, value={value}")

some_method_kwargs(param1=1, param2="string", param3=[1, 2, 3], param4={"key": "value"})
users = [{"name": "Bob", "age": 30}, {"name": "Ana", "age": 20}, ]
sorted_users = list(sorted(users, key=lambda user: user["age"]))
print(f"sorted_users={sorted_users}")

def add(a, lst=[]):
    lst.append(a)
    return lst

add(1)
add(22)
add(4)
print(add(3))

def add_not_agg(v, arr=None):
    if arr is None: arr = []
    arr.append(v)
    return arr

arr_init = []
add_not_agg(1, arr_init)
add_not_agg(22, arr_init)
add_not_agg(4, arr_init)
print(add_not_agg(3, arr_init))

sorted_users = sorted(users, key=lambda u: u["age"])
list_numbers = [5, 2, 9, 1, 5, 6]
list_sorted_with_lambda = sorted(list_numbers, key=lambda z: -z)
print(f"list_sorted_with_lambda={list_sorted_with_lambda}")
city_name = {"Ukraine": "Kiev", "USA": "Washington", "France": "Paris"}
print(sorted(city_name, key=lambda u: city_name[u]))

try:
    num = int(input("Введіть позитивне число: "))
    print("Подвоєне значення:", num * 2)
except ValueError:
    print("Помилка: введено не число.")

