def longest(a1, a2):
    result_list = list(set(list(a1) + list(a2)))
    result_list.sort()
    return "".join(result_list)
