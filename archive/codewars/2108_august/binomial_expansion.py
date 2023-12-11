import pytest

import math
import re


def binomial_coef(n, k):
    return math.factorial(n) / (math.factorial(n - k) * math.factorial(k))


def expand(expr):
    list_num = re.findall(r'[-]?\d+', expr)
    variable_name = re.findall(r'[a-z]', expr)[0]
    signs = re.findall(r'[-,+]', expr)
    if len(signs) == 1:
        first_sign = ""
    else:
        first_sign = signs[0]
    if len(list_num) == 2:
        list_num.insert(0, int(first_sign + str(1)))
    a = int(list_num[0])
    b = int(list_num[1])
    degree = int(list_num[2])

    res_str = ""
    rng = range(degree, -1, -1)
    for num in rng:
        coef = int(binomial_coef(degree, num))*int(math.pow(a,num))*int(math.pow(b,degree-num))

        if coef < 0:
            sign = ""
        else:
            sign = "+"

        # if coef is 1 or -1 replace it with sign
        if (coef == 1 or coef == -1) and num != 0:
            coef = str(coef).replace("1", "")

        if num == degree and num != 1:
            incr = f"{coef}{variable_name}^{num}"
        elif num == 0:
            # dont show variable if power is 0 : 1x^0 = 1
            incr = f"{sign}{coef}"
        elif num == 1:
            # if power is 1 replace power sign : 2x^1 = 2x
            if num == degree and sign == "+":
                # dont show + if it first member
                incr = f"{coef}{variable_name}"
            else:
                incr = f"{sign}{coef}{variable_name}"
        else:
            # usual case : -128x^3
            incr = f"{sign}{coef}{variable_name}^{num}"
        res_str = res_str + f"{incr}"
    if degree == 0:
        return "1"
    else:
        return res_str


# assert expand("(1m-3)^2") == "m^2-6m^1+9"
# assert expand("(1m+3)^2") == "m^2+6m^1+9"
# assert expand("(2m-3)^2") == "4m^2-12m^1+9"
# assert expand("(-2m+3)^2") == "4m^2-12m^1+9"
# assert expand("(-2m-3)^2") == "4m^2+12m^1+9"
# assert expand("(m+1)^3") == "4m^2-12m^1+9"
# assert expand("(-2m-3)^2") == "4m^2-12m^1+9"

print("----------------")
# print(expand("(x-1)^1"))
print(expand("(2x-1)^13"))
print(expand("(2x+1)^3"))
print(expand("(-2x-1)^3")) #-1 only for coef =1
print(expand("(-2x+1)^3")) #-1
# print(expand("(x-1)^3"))

# print(expand("(-x+1)^1"))
# print(expand("(x-1)^1"))

"(-5s+20)^0"
"(-u-18)^5"


# print(expand("(1m-3)^2"))
#print(expand("(3m+2)^2"))
# expand("(-5m+3)^4")
# expand("(-5m-13)^4")
