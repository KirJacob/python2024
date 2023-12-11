def convert_word(word):
    if word == "?" or word == "!":
        return word
    else:
        return word[1:len(word)] + word[0] + "ay"


def pig_it(text):
    return " ".join(list(map(lambda x: convert_word(x), list(text.split()))))


# your code here
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


# print(pig_it("hello there people"))
print(pig_it("Pig latin is cool !"))
# print("Argentina"[::-1])
word = "Ukraine"
print(word[1:len(word)] + word[0])
