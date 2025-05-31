def maskify(cc):
    temp = list(cc)
    temp_size = len(temp)
    for i in range(temp_size - 1, -1, -1):
        if temp_size - i > 4:
            temp[i] = "#"
    return "".join(temp)
