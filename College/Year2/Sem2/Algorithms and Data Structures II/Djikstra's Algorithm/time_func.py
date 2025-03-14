from time import perf_counter

# function that takes in another function and it's arguments
# and returns a tuple with (function execution time, function result)
def time_func(func, *args, **kwargs):
    start_time = perf_counter()
    res = func(*args, **kwargs)
    end_time = perf_counter()
    exec_time = end_time - start_time
    return exec_time, res
