# from preloaded import MORSE_CODE


def decode_morse(morse_code):
    MORSE_CODE = {}
    morse_code = morse_code.strip()
    morse_code = morse_code.replace("   ", " space ")
    letter_list = morse_code.split(" ")
    MORSE_CODE["space"] = " "
    codes = MORSE_CODE.keys()
    decoded = list(map(lambda x: MORSE_CODE[x], letter_list))
    result = "".join(decoded)
    return result