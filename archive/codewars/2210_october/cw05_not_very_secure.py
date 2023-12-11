def alphanumeric(password):
    print(f"password={password}")
    password = password.lower()
    alpha_numeric = list(range(48, 58)) + list(range(97, 123))
    alpha_numeric_chr = list(map(lambda element: chr(element), alpha_numeric))
    if password == "":
        return False
    for symbol in list(password):
        print(f"symbol={symbol}")
        if not alpha_numeric_chr.__contains__(symbol):
            return False
    return True

print(alphanumeric('6ppAYtKj9nYzO11DVUPJbbnaf4'))

for element in list(range(48, 58)) + list(range(97, 123)):
    print(f"code={element} chr={chr(element)}")


# pattern = re.compile('^[0-9a-zA-Z]+$')
# def alphanumeric(string):
#   return pattern.match(string) is not None



