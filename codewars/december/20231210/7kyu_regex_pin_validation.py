import re


def validate_pin(pin):
    if pin.__contains__('\n'):
        return False
    return bool(re.match(r"^(?:\d{4}|\d{6})$", pin))
