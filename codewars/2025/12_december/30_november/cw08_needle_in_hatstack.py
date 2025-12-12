from codewars.utils.decorators import exec_time

def find_needle(haystack):
    for index in range(0, len(haystack)):
        if "needle" == haystack[index]:
            return f"found the needle at position {index}"

@exec_time
def test_delete_nth():
    assert find_needle(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]) == 'found the needle at position 3'


test_delete_nth()