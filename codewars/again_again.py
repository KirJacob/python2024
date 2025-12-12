import time
import math

# decorator example

def exec_time(func):
    def wrapper(*args, **kwargs):
        start_ts = time.time()
        result = func(*args, **kwargs)
        exec_ms = time.time() - start_ts
        print(f"exec_time {exec_ms}")
        return result
    return wrapper

@exec_time
def iterate_long(degree):
    agg = 0
    for index in range(0, int(math.pow(10, degree))):
        agg = agg + index
    print(agg)

iterate_long(5)

# generator example

def generate_num(num):
    for index in range(num):
        yield index

gen_var = generate_num(100)

print(next(gen_var))
print(next(gen_var))
print(next(gen_var))


