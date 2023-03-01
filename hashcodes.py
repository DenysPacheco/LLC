import hashlib
import time
import random

# Simple hash value

def hashy(value):
    return hashlib.sha256(str(value).encode()).hexdigest()


# ⚠️ I know 'random.random()' is faster and better for just 6 digits codes over 10**9 runs but I wanted to implement something based on time and changeable between calls


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


# print(random_hash(8))
# print(random_hash(6))
# print(random_hash(4))

# start = time.time()

# for x in range(1000000):
#     random_hash(6)

# end = time.time()

# print(f"{(end-start):.2f} secs")

# 😲 Learning is the way: 'random.seed' is bad for this!
# plus, this one is faster and safer

def random_sha256(size: int) -> str:
    """Makes a random alphanumeric sha256 hashed string.

    Args:
        size (int): size of the hash string

    Returns:
        str: alphanumeric hash string
    """
    # encode to the hash function
    enc_rand = str(random.random()).encode()
    # hash it using sha256
    hashed = hashlib.sha256(enc_rand)
    # digests and splits the last chars with size
    dec_hash = hashed.hexdigest()[-size:]

    return dec_hash

    # compact
    # return hashlib.sha256(str(random.random()).encode()).hexdigest()[-size:]


# start = time.time()

# for x in range(1000000):
#     random_sha256(12)

# end = time.time()

# print(f"{(end-start):.2f} secs")
