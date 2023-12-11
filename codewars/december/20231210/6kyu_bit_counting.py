def count_bits(n):
    binary = format(n, 'b')
    list_of_nums = list(map(lambda num: int(num), list(str(binary))))
    return sum(list_of_nums)
