import re


def to_camel_case(text):
    lst = re.split('-|_', text)
    is_not_capitalized = lst[0].lower() == lst[0]
    lst_changed = list(map(lambda x: str(x).capitalize(), lst))
    if is_not_capitalized:
        lst_changed[0] = lst_changed[0].lower()
    return "".join(lst_changed)


print(to_camel_case("the_stealth_warrior"))
# to_camel_case("the-stealth-warrior")
# to_camel_case("the_stealth_warrior")
# to_camel_case("thestealthwarrior")
# print("comparison=" + str('b' == 'a'))
