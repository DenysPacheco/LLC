#https://www.codewars.com/kata/58aa8368ae929ea2e00000d9/python

def combs(n):
    from itertools import combinations
    l = []
    for x in range(1, n+1):
        l += [tup [::-1] for tup in combinations(list(range(1,n+1)), x)]
    l.sort()
    return l

def pow5(n):
    if type(n) is int:
        return 5**n
    if type(n) is tuple:
        return sum(map(pow5, n))
    if type(n) is list:
        return list(map(pow5, n))

def chandos(n):
    c = combs(n.bit_length())[n-1]
    return pow5(c)
    
