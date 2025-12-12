import time


def my_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"execution time: {elapsed:.10f} secs")
        return result
    return wrapper