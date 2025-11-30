import time


def my_decorator_template(func):
    def wrapper(*args, **kwargs):
        result = func(args, kwargs)
        return result
    return wrapper


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        print(f"\nCalling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"execution time : {elapsed:.10f} seconds")
        return result
    return wrapper
