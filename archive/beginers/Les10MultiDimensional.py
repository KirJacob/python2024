import Les0MyHelper
#  Lesson 10 - Multidimensional array

# Task - 2
# Transpone matrix

b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
c = [[10, 11, 12, 13],
     [14, 15, 16, 17],
     [18, 19, 20, 21]]
d = [[101, 102, 103],
     [111, 112],
     [121, 122, 123, 124]]


def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()


def mirror_array(matrix):
    for i in range(len(matrix)):
        width = len(matrix[i])
        # halfed = round(width / 2)
        halfed = width // 2  # // - is making division without decimals
        for j in range(halfed):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][width - j - 1]
            matrix[i][width - j - 1] = temp
    return matrix


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def mirror_2d_arr(arr_2d):
    for arr in arr_2d:
        for i in range(len(arr) // 2):
            swap(arr, i, len(arr) - 1 - i)


Les0MyHelper.separator()
print_matrix(c)
Les0MyHelper.separator()
print_matrix(mirror_array(c))
Les0MyHelper.separator()
print_matrix(d)
Les0MyHelper.separator()
print_matrix(mirror_array(d))
Les0MyHelper.separator("mirror_2d_arr")
mirror_2d_arr(d)
print_matrix(d)
