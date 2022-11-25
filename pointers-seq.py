# Kinda hard hehe
# source: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

def solution(lis: list) -> str:
    string = ''
    curr = 0
    point = 0
    nex = point + 1
    
    #for index, item in enumerate(lis):
    #    print(f"{index}:{item}, ", end=' ')
    
    while curr < len(lis) - 1:
        #print()
        #print('bf', curr, point, nex, string)
        
        if lis[point] != lis[nex] - 1:
            string += f"{lis[curr]},"
        
        while nex < len(lis) and lis[point] == lis[nex] - 1:
            point += 1
            nex = nex + 1 if nex < len(lis) - 1 else len(lis) - 1
            #print('inside', curr, point, nex, string)
            continue
            
        if curr < point and point < nex or nex == len(lis)-1:
            if lis[curr] < lis[point]-1:
                string += f"{lis[curr]}-{lis[point]},"
            else:
                string += f"{lis[curr]},{lis[point]},"
            
        curr = nex
        point = nex
        nex = nex + 1 if nex < len(lis) - 1 else len(lis) - 1
        #print('af', curr, point, nex, string)
        #continue
            
    
    return string[:-1]
    
    
#print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))

print(solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]) == "-10--8,-6,-3-1,3-5,7-11,14,15,17-20")
