def descending_order(number):
    list_num = list(map(lambda num: int(num), list(str(number))))
    list_num.sort(reverse=True)
    list_str = list(map(lambda num: str(num), list_num))
    return int("".join(list_str))


print(descending_order(1232338346))


def to_jaden_case(string):
    return " ".join(list(map(lambda word: str(word).capitalize(), string.split(" "))))


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))


def is_isogram(string):
    list_lower = list(map(lambda letter: letter.lower(), list(string)))
    return not len(list_lower) - len(set(list_lower)) > 0


print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))




