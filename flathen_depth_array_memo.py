from hashlib import sha256

def hashy(value):
    return sha256(str(value).encode()).hexdigest()

'''
if hash(arr) in table:
    return table[hash(arr)]
else:
    toMemo = calculate()
    table.update(hash(toMemo): toMemo)
    return toMemo
'''

arr = [1, [2, [3, [4, [5, [6, [7, 8, 9]]]]]]]

dic_flat = {}
def flatten(arr):
    if not arr: return arr
    if hashy(arr) in dic_flat: return dic_flat[hashy(arr)]
    if isinstance(arr[0], list):
        res = flatten(arr[0]) + flatten(arr[1:])
        dic_flat.update({hashy(arr): res})
        return res
    return arr[:1] + flatten(arr[1:])
    
dic_depth = {}
def depth(arr):
    if not arr: return 0
    if hashy(arr) in dic_depth: return dic_depth[hashy(arr)]
    if isinstance(arr, list):
        print('map', arr, *map(depth, arr))
        res = 1 + max(map(depth, arr))
        dic_depth.update({hashy(arr): res})
        return res
    else:
        return 0
    
print(flatten(arr))
print(depth(arr))
