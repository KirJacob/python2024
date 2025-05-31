def method():
    hey = "name"
    print(f"{hey} you!")


class Animal:

    def __init__(self, breed):
        self.breed = breed


Animal("hound")

lst = [1, 2, 3, 4]
for i in lst:
    print(i)

lst_filtered = list(map(lambda x: x * 2, lst))
print(lst_filtered)
