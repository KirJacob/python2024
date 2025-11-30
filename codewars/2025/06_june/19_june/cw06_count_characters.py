def count(s):
    result_map = {}
    for symbol in set(list(s)):
        result_map[symbol] = len(list(filter(lambda x: x == symbol, list(s))))
    return result_map


def test_count():
    assert count('aba') == {'a': 2, 'b': 1}
    assert count('') == {}
    assert count('aa') == {'a': 2}
    assert count('aabb') == {'b': 2, 'a': 2}

# print(count('abaabc'))
