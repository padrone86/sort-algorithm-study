from functools import wraps
import time


def stop_watch(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} 実行時間: {end - start}")
        return result
    return wrapper
