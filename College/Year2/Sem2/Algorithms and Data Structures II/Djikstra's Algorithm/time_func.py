from time import perf_counter

def time_func(func, *args, **kwargs):
    start_time = perf_counter()
    res = func(*args, **kwargs)
    end_time = perf_counter()
    print(f"{func.__name__} took {(end_time - start_time):.8f}s to execute")
    return res
