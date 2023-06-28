import re
from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(
            f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper

dprime = {}

@timeit
def regPrime(m):
    reg = r'^1?$|^(11+?)\1+$'
    for n in range(m):
        if n not in dprime:
            res = re.match(reg, '1'*n) == None
            dprime.update({n: res})
            #if res: print(m, res)

regPrime(10**1)
regPrime(10**2)
regPrime(10**3)
#regPrime(10**4)

print(len(dprime))
