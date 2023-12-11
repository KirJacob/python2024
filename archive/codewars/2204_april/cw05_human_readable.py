import math


def number_format(number):
    if number < 10:
        return "0" + str(number)
    else:
        return number


def make_readable(seconds):
    hours = math.floor(seconds / 3600)
    seconds = seconds - hours * 3600
    minutes = math.floor(seconds / 60)
    seconds = seconds - 60 * minutes
    formatted_time = f"{number_format(hours)}:{number_format(minutes)}:{number_format(seconds)}"
    return formatted_time


print(make_readable(8245))
print(make_readable(2300))