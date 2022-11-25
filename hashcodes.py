import time
import random


def random_hash(digits: int) -> str:
    """Generate string of random numeric integers (every call is unique)

    Args:
        digits (int): number of digits of the string

    Returns:
        str: random numeric digits
    """

    # take time
    ms = time.time()

    # split last 4 microseconds
    rms = str(ms)[-4:]

    # use it as seed
    random.seed(rms)

    # take last digits from random
    rhash = str(hash(random.random()))[-digits:]

    return rhash


print(random_hash(8))
print(random_hash(6))
print(random_hash(4))

start = time.time()

for x in range(1000000):
    random_hash(6)

end = time.time()

print(f"{(end-start):.2f} secs")
