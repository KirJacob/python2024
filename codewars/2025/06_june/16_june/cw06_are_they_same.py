from codewars.decorators_helper import exec_time


def comp(array1, array2):
    if len(array1) != len(array2):
        return False
    else:
        for element in array1:
            removed_element = element * element
            if array2.__contains__(removed_element):
                array2.remove(removed_element)
        if len(array2) == 0:
            return True
        else:
            return False


@exec_time
def test_comp():
    assert comp([121, 144, 19, 161, 19, 144, 19, 11],
                [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
                ) == True

    assert comp([121, 144, 19, 161, 19, 144, 19, 11],
                [11 * 21, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
                ) == False

    assert comp([121, 144, 19, 161, 19, 144, 19, 11],
                [11 * 11, 121 * 121, 144 * 144, 190 * 190, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
                ) == False
