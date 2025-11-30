def tower_builder(n_floors):
    empty = " "
    star = "*"
    empty_side = n_floors - 1
    star_side = 1
    result_list = []
    for index in range(n_floors):
        floor = empty * empty_side + star * star_side + empty * empty_side
        result_list.append(floor)
        empty_side = empty_side - 1
        star_side = star_side + 2
    return result_list
