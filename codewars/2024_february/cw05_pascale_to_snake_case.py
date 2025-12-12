def to_underscore(string):
    str_lst = list(str(string))
    for i in range(0, len(str_lst)):
        if str(str_lst[i]).isupper() and i != 0:
            str_lst[i] = f"_{str_lst[i]}"
    str_list_split = "".join(str_lst).split("_")
    str_list_split_lowered = list(map(lambda word: word.lower(), str_list_split))
    return "_".join(str_list_split_lowered)


def test_positive():
    assert to_underscore("TestController") == "test_controller"
    assert to_underscore("MoviesAndBooks") == "movies_and_books"
    assert to_underscore("App7Test") == "app7_test"
    assert to_underscore(1) == "1"
