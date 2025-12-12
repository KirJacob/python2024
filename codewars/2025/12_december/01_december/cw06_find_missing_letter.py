def find_missing_letter(chars):
    letter_codes = list(map(lambda x: ord(x), chars))
    missing_index_after = list(filter(lambda index: letter_codes[index + 1] - letter_codes[index] > 1, list(range(0, len(chars) - 1))))[0]
    return chr(letter_codes[missing_index_after] + 1)

def test_find_missing_letter():
    assert find_missing_letter(['a', 'b', 'c', 'd', 'f']) == 'e'
    assert find_missing_letter(['O', 'Q', 'R', 'S']) == 'P'
    assert find_missing_letter(['b', 'd']) == 'c'

print(find_missing_letter(['a', 'c', 'd', 'e', 'f']))