def count_smileys(arr):
    def verify_smile(smile_str):
        nose = ''
        if len(smile_str) == 2:
            mouth = smile_str[1]
        elif len(smile_str) == 3:
            nose = smile_str[1]
            mouth = smile_str[2]
        else:
            return False
        eyes = smile_str[0]
        if not(eyes == ':' or eyes == ';'):
            return False
        if not(nose == '' or nose == '-' or nose == '~'):
            return False
        if not(mouth == ')' or mouth == 'D'):
            return False
        return True
    return len(list(filter(lambda smile: verify_smile(smile), arr)))


def test_count_smileys():
    assert count_smileys([]) == 0
    assert count_smileys([':D', ':~)', ';~D', ':)']) == 4
    assert count_smileys([':)', ':(', ':D', ':O', ':;']) == 2
    assert count_smileys([';]', ':[', ';*', ':$', ';-D']) == 1


print(count_smileys([':D', ':~)', ';~D', ':)']))

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D