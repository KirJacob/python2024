# recap lists
list = [1,2,34]
print(list)
list.append(100)
list.pop(0)
print(list)
print((list[0]))

# recap sets


# recap tuples


l = ["Bob", "Rolf", "Anne"]  # can remove and add, order is kept
t = ("Bob", "Rolf", "Anne")  # cannot remove or add elements in tuple, order is kept
s = {"Bob", "Rolf", "Anne"}  # element is unique, order is not guaranteed
print(l[0])
print(t[0])  # subscript notation
print("Bob" in s)
l[0] = "Smith" # cannot do this on a tuple as well as
l.remove("Rolf")
print(l)
s.add("Smith")
s.add("Smith")
print(s)

# advanced set operations
friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}
print(f"intersection={friends.intersection(abroad)}")
print(f"difference={friends.difference(abroad)}")
print(f"difference={abroad.difference(friends)}")
print(f"union={friends.union(abroad)}")

science = {"Bob", "Jen", "Rolf", "Charlie"}
art = {"Bob", "Jen", "Adam", "Anne"}
print(science.intersection(art))




