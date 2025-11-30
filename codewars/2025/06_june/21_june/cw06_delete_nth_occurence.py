def delete_nth(order, max_e):
    length = len(order)
    occurence_map = {}
    res_list = []
    for index in range(length):
        element = order[index]
        if element in occurence_map.keys():
            if occurence_map[element] < max_e:
                res_list.append(element)
            occurence_map[element] = occurence_map[element] + 1
        else:
            occurence_map[element] = 1
            res_list.append(element)
    return res_list


def test_delete_nth():
    assert delete_nth([20, 37, 20, 21], 1) == [20, 37, 21]
