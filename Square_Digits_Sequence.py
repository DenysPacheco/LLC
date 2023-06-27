#https://www.codewars.com/kata/5886d65e427c27afeb0000c1

def sumSquares(l: list) -> int:
    return sum([int(x)**2 for x in l])
    
def splitList(n: int) -> int:
    l = list(map(int, str(n)))
    return sumSquares(l)

def solve(n: int) -> int:
    occ = []
    if n == 0: return 1
    while n not in occ:
        occ.append(n)
        n = splitList(n)
    return len(occ) + 1

print(solve(16)) #9
print(solve(0)) #1

occ = list(map(solve, range(100)))
mega = max(occ)
print(occ, mega, occ.index(mega)) #[1, 2, 10, 14, 9, 13, 18, 7, 14, 13] 18 6
