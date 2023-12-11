def is_pangram(s):
    letters_lst = list(map(lambda letter: letter.lower(), list(s)))
    for code in range(97, 123):
        if not(chr(code) in letters_lst):
            return False
    return True


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))
