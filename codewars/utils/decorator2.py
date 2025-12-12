import time

def exec_time_second(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(args, kwargs)
        end_time = time.time()
        print(f"exec_time={end_time - start_time}")
        return result
    return wrapper