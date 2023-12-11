def first_non_repeating_letter(string):
    string_list = list(string)
    string_list_lower = list(map(lambda x: x.lower(), string_list))
    string_set = set(string_list_lower)
    one_symbol_list = list(filter(lambda x: len(list(filter(lambda y: x == y, string_list_lower))) == 1, string_set))
    result_list = list(filter(lambda x: x.lower() in one_symbol_list, string_list))
    if len(result_list) == 0:
        return ""
    else:
        return result_list[0]


string_sample = "aabbcc"
string_sample = "sTreSS"
print(first_non_repeating_letter(string_sample))
