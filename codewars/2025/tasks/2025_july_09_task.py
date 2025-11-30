# Revert a string: Given a string s = "iamstring" , make it s = "gnirtsmai"
# Revert a dictionary: Given a dictionary like d = {'a': 1, 'b': 2}, make it     {1: 'a', 2: 'b'}



# s = "iamstring"
# s_list = list(s)
# s_list.reverse()
# result = "".join(s_list)
# print(result)


# Revert a dictionary: Given a dictionary like d = {'a': 1, 'b': 2}, make it     {1: 'a', 2: 'b'}

d = {'a': 1, 'b': 2}

result = {}
for element in d.keys():
    result[d[element]] = element

print(result)