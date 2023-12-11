def find_short(s):
    return min(list(map(lambda w: len(w), s.split(" "))))
