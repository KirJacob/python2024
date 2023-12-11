import math


def isPP(n):
    for index in range(2, round(n/2) + 1):
        if n % index == 0:
            log_res = round(math.log(n, index), 8)
            if math.floor(log_res) - log_res == 0:
                return [index, math.floor(log_res)]
    return None


print(isPP(274794888224))
