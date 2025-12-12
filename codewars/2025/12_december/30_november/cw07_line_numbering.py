from codewars.utils.decorators import exec_time

@exec_time
def number(lines):
    for index in range(0, len(lines)):
        lines[index] = f"{index + 1}: {lines[index]}"
    return lines

def test_number():
    assert number(["a", "b", "c"]) == ["1: a", "2: b", "3: c"]
    assert number([]) == []

test_number()