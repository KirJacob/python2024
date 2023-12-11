x = (5, 11)
y = 5, 11
z = [(1, 2), [2, 3]]
print(y[1])
print(z[0][1])
z = 11, 21
b, a = z
print(b, a)

friend_ages = {"Rolf": 24, "Kirill": 41, "Adam": 35}
print(friend_ages.items())

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"name={name} age={age} profession={profession}")

for person in people:
    print(f"name={person[0]} age={person[1]} profession={person[2]}")

person = ("Bob", 42, "Mechanic")
name, _, profession = person  # _ means ignored variable which doesnt matter

head, *tail = [1, 2, 3, 4, 5]
print(head, tail)
list = [1, 2, 3]
head_list, *tail_list = list
print(head_list, tail_list)
*head_list2, tail_list2 = list
print(head_list2, tail_list2)


