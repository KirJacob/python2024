def generate_hashtag(s):
    if s == '':
        return False
    lst_filtered = list(filter(lambda x: x != '', s.split(" ")))
    lst_capitalized = list(map(lambda x: x.capitalize(), lst_filtered))
    result = "#" + "".join(lst_capitalized)
    if len(result) > 140:
        return False
    else:
        return "#" + "".join(lst_capitalized)