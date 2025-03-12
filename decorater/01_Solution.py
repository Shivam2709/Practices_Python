# Problem: Write a decorator that measures the time a function takes to execute.

import time

def timer(func):
    def wapper(*agrs, **kwargs):
        start = time.time()
        result = func(*agrs, **kwargs)
        end = time.time()
        print(f"{func.__name__} run in {end - start} time")
        return result
    return wapper

@timer
def Example_function(n):
    time.sleep(n)

Example_function(2)