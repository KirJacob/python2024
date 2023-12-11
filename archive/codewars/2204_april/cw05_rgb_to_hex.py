def rgb(r, g, b):
    return hex_conv(r) + hex_conv(g) + hex_conv(b)


def hex_conv(number):
    if number < 0:
        number = 0
    elif number > 255:
        number = 255
    result = hex(number).replace("0x", "").upper()
    if len(result) == 1:
        result = "0" + result
    return result
