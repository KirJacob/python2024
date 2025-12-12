def find_outlier(integers):
    res_list_odd = [num for num in integers if num % 2 == 0]
    res_list_even = [num for num in integers if num % 2 != 0]
    return res_list_odd[0] if (len(res_list_even) > len(res_list_odd)) else res_list_even[0]


# TESTS
# [2, 4, 0, 100, 4, 11, 2602, 36] -->  11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21] --> 160 (the only even number)


sample_odd = [2, 4, 0, 100, 4, 11, 2602, 36]
sample_even = [160, 3, 1719, 19, 11, 13, -21]

# print(find_outlier(sample_odd))
print(find_outlier(sample_even))
#find_outlier(sample_even)


