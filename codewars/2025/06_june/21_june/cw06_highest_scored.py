def score_chr(symbol):
    return ord(symbol) - 96


def score_word(word):
    score_list = [score_chr(x) for x in list(word)]
    return sum(score_list)


def high(x):
    temp_list = x.split(" ")
    max_score = score_word(temp_list[0])
    max_word = temp_list[0]
    for word in temp_list:
        if score_word(word) > max_score:
            max_word = word
            max_score = score_word(max_word)
    return max_word
