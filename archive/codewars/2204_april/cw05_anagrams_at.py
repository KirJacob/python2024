def sort_to(word_parameter):
    lst = list(word_parameter)
    lst.sort()
    return lst


def anagrams(word, words):
    result = []
    word_to_compare = sort_to(word)
    for word_member in words:
        word_str = word_member
        word_lst = sort_to(word_member)
        if word_to_compare == word_lst:
            result.append(word_str)
    return result


print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))


