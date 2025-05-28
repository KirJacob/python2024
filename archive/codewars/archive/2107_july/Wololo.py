def alphabet_war(fight):

    right_power = {"m": 4, "q": 3, "d": 2, "z": 1, "j": 0}
    left_power = {"w": 4, "p": 3, "b": 2, "s": 1, "t": 0}
    list_letters = list(fight)

    def check_num_priest(letter):
        if letter in left_power and left_power[letter] == 0:
            return "left"
        if letter in right_power and right_power[letter] == 0:
            return "right"
        return "nobody"

    def check_priest_win(list, num, size):
        if size == 1:
            if list[0] in left_power:
                return "left"
            elif list[0] in right_power:
                return "right"
            else:
                return "nobody"
        elif num == 0:
            right_ngbr = list[num + 1]
            return check_num_priest(right_ngbr)
        elif num == size - 1:
            left_ngbr = list[num - 1]
            return check_num_priest(left_ngbr)
        else:
            right_ngbr = list[num + 1]
            left_ngbr = list[num - 1]
            if (check_num_priest(right_ngbr) == "right" and check_num_priest(left_ngbr) != "left") \
                    or (check_num_priest(left_ngbr) == "right" and check_num_priest(right_ngbr) != "left"):
                return "right"
            if (check_num_priest(right_ngbr) == "left" and check_num_priest(left_ngbr) != "right") \
                    or (check_num_priest(left_ngbr) == "left" and check_num_priest(right_ngbr) != "right"):
                return "left"
            return "nobody"

    score_left = 0
    score_right = 0

    for num in range(len(list_letters)):
        letter = list_letters[num]
        if letter in left_power:
            if check_priest_win(list_letters, num, len(list_letters)) == "right":
                score_right += left_power[letter]
            else:
                score_left += left_power[letter]
        if letter in right_power:
            if check_priest_win(list_letters, num, len(list_letters)) == "left":
                score_left += right_power[letter]
            else:
                score_right += right_power[letter]

    result = "Let's fight again!"
    if score_left > score_right:
        result = "Left side wins!"
    elif score_right > score_left:
        result = "Right side wins!"
    print(f"fight={fight} result={result}")
    return result

# left_power = {"m": 4, "q": 3, "d": 2, "z": 1, "j": 0}
# right_power = {"w": 4, "p": 3, "b": 2, "s": 1, "t": 0}
# test.assert_equals( alphabet_war("z") , "Right side wins!" );
# test.assert_equals( alphabet_war("tz") , "Left side wins!" );
# test.assert_equals( alphabet_war("jbdt") , "Let's fight again!" );
# test.assert_equals( alphabet_war("jz") , "Right side wins!" );
# test.assert_equals( alphabet_war("zt") , "Left side wins!" );
# test.assert_equals( alphabet_war("sj") , "Right side wins!" );
# test.assert_equals( alphabet_war("azt") , "Left side wins!" );
# test.assert_equals( alphabet_war("tzj") , "Right side wins!" );
# test.assert_equals( alphabet_war("wololooooo") , "Left side wins!" );
# test.assert_equals( alphabet_war("zdqmwpbs") , "Let's fight again!" );
# test.assert_equals( alphabet_war("ztztztzs") , "Left side wins!" );

alphabet_war("z")
alphabet_war("tz")  # wrong should be left not right
alphabet_war("jbdt")
alphabet_war("jz") # wrong should be right not left
alphabet_war("zt")
alphabet_war("sj")
alphabet_war("azt")
alphabet_war("tzj")
alphabet_war("wololooooo")
alphabet_war("zdqmwpbs")
alphabet_war("ztztztzs")
