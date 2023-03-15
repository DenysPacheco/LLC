# kata: https://www.codewars.com/kata/5e1ab1b9fe268c0033680e5f

from math import sqrt, ceil
from timeitWrapper import timeit
import numpy as np


def triangle(index):
    return int(index*(index+1)/2)


def reverse_triangle(num):
    return ceil(sqrt(2*num + 1/4) - 1/2)


def size(block):
    aux = [int('9'*c) if c else 0 for c in range(len(str(block)))]
    return sum([triangle(block-dozens) for dozens in aux])


def sumSequence(num):
    return (sum(range(1, num)))


@timeit
def sequence(num):
    return ''.join(map(str, np.arange(1, num+1).tolist()))


def find(n, arr, start):
    if n < start:
        return False
    return arr[n-start]


@timeit
def solve(n):
    if n <= 0:
        return False
    block = reverse_triangle(n)
    start = size(block-1)+1
    gambiarra = 0
    while n-start < 0:
        start = size(block-gambiarra)+1
        gambiarra += 1
    # print(gambiarra)
    arr = sequence(block)
    # debug
    # print(f"#{n}, block:{block}, start:{start}, pos:{n-start}, len:{len(arr)}, size:{size(block-1)}, arr:{arr}, res: {arr[n-start]}")
    return int(arr[n-start])
    
    # another way
    '''
    if n <= 0: return False
    block = reverse_triangle(n)
    total = size(block)
    arr = sequence(block)
    while total - n > len(arr):
        block -= 1
        total = size(block)
    arr = sequence(block)
    return int(arr[-(total-n+1)%len(arr)])
    '''

# assertion algorithm
# arrres = []
# for x in range(1, 120 + 1):
#     pass
#     #print(x, triangle(x), reverse_triangle(x))
#     arrres += ''.join([str(w) for w in range(1, x+1)])
#     #print(f"{x}, t:{triangle(x)}, s:{size(x)}, arr:{len(''.join(arrres))}")

# for x in range(1, 2100):
#     print('esp:', arrres[x-1], solve(x) == arrres[x-1], ''.join(arrres[:size(reverse_triangle(x))]))


# tests
print(solve(1) == 1)
print(solve(2) == 1)
print(solve(3) == 2)
print(solve(100) == 1)
print(solve(2100) == 2)
print(solve(31000) == 2)
# hard tests
#print(solve(999999999999999999) == 4)
#print(solve(1000000000000000000) == 1)
#print(solve(999999999999999993) == 7)
