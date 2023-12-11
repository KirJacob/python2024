def opposite(first, second):
    if {str.lower(first), str.lower(second)} == {"north", "south"}:
        return True
    elif {str.lower(first), str.lower(second)} == {"west", "east"}:
        return True
    else:
        return False


def loop(arr):
    print("loop=" + str(arr))
    result = []
    flag = False
    for num in range(0, len(arr)):
        first = arr[num]
        if num == int(len(arr)) - 1:
            if not flag:
                result.append(first)
            return result
        else:
            second = arr[num + 1]
        # print(str(num) + "|" + arr[num] + "|" + str(first) + "|" + str(second) + "|" + str(opposite(first, second)) +
        #       "|" + str(result) + "|" + str(arr))
        if flag:
            flag = False
        elif opposite(first, second):
            flag = True
        else:
            result.append(first)
    return result


def dir_reducer(arr):
    print("init=" + str(arr))
    arr_init = arr
    arr_reduced = arr
    start = True
    while start or len(arr_reduced) < len(arr_init):
        start = False
        arr_init = arr_reduced
        arr_reduced = loop(arr_reduced)
    return arr_reduced


arr01 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# arr02 = ["SOUTH", "NORTH", "WEST"]
# arr03 = ["SOUTH"]

# arr01 = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTH', 'NORTH', 'SOUTH', 'NORTH', 'WEST', 'EAST']

# print(dir_reducer(arr01))
# print(loop(arr01))
# print(loop(arr02))
# print(loop(arr03))

