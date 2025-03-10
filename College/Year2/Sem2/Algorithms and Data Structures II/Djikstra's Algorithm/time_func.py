from time import perf_counter

def time_func(func, *args, **kwargs):
    start_time = perf_counter()
    res = func(*args, **kwargs)
    end_time = perf_counter()
    exec_time = end_time - start_time
    return exec_time, res
