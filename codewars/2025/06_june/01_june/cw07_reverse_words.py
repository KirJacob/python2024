def reverse_words(text):
    words = text.split(" ")
    reversed = list(map(lambda w: w[::-1], words))
    return " ".join(reversed)


def test_reserve_words():
    assert reverse_words('The quick brown fox jumps over the lazy dog.') == 'ehT kciuq nworb xof spmuj revo eht yzal .god'
    assert reverse_words('apple') == 'elppa'
    assert reverse_words('a b c d') == 'a b c d'
