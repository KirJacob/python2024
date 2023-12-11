# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
# spinWords( "This is a test") => returns "This is a test"
# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    rev_list = list(map(lambda word: word if len(word) < 5 else word[::-1], sentence.split(" ")))
    return " ".join(rev_list)


print(spin_words("Hey fellow warriors"))
