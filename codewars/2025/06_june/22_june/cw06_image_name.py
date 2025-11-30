import random
import string


def generateName():
    random_word = []
    for index in range(6):
        random_letter = str(random.choice(string.ascii_letters)).capitalize()
        random_word.append(random_letter)
    result = "".join(random_word)
    return result

