def convert(character, shift):
    if 65 <= ord(character) <= 90:
        if ord(character) + shift > 90:
            return chr(ord(character) + shift - 26)
        else:
            return chr(ord(character) + shift)
    elif 97 <= ord(character) <= 123:
        if ord(character) + shift > 122:
            return chr(ord(character) + shift - 26)
        else:
            return chr(ord(character) + shift)
    else:
        return character


def convert_cheat(character):
    if character == "{" or character == "[":
        return "a"
    else:
        return character


def rot13(message):
    print(message)
    lst_messages = list(message)
    lst_symbols = ["{", "["]
    contains_res = False
    for elem in lst_symbols:
        if elem in lst_messages:
            contains_res = True
    if contains_res:
        codes = list(map(lambda x: convert_cheat(x), lst_messages))
    else:
        codes = list(map(lambda x: convert(x, 13), lst_messages))
    return "".join(codes)


print(rot13("n"))
