import re


def increment_string(strng):
    if strng == "":
        return "1"
    else:
        reg_search = re.search("[A-Za-z]+", strng)
        # no letters
        if reg_search is None:
            incremented = int(strng) + 1
            diff = len(strng) - len(str(incremented))
            return "0" * diff + str(incremented)
        else:
            numbers_part = re.search("(\\d+)(?!.*\\d)", strng).group(0)
            first_part = strng.replace(numbers_part, "")

        # with numbers
        if len(numbers_part) > 0:
            incremented = int(numbers_part) + 1
            diff = len(numbers_part) - len(str(incremented))
            # print(f"letters_part={letters_part} numbers_part={numbers_part} incremented={incremented} diff={diff}")
            incremented = "0" * diff + str(incremented)
        else:
            # without numbers
            incremented = 1
        return letters_part + str(incremented)


print(increment_string("3364`?798o#5k34739,PF_5559912z \p5[d961U8rji1782200k\4652084000000989"))
# print(increment_string("009"))

# test.assert_equals(increment_string("foo"), "foo1")
# test.assert_equals(increment_string("foobar001"), "foobar002")
# test.assert_equals(increment_string("foobar1"), "foobar2")
# test.assert_equals(increment_string("foobar00"), "foobar01")
# test.assert_equals(increment_string("foobar99"), "foobar100")
# test.assert_equals(increment_string("foobar099"), "foobar100")
# test.assert_equals(increment_string(""), "1")
