#find the most depth of an inner nested array

arr = [1, [2, [3, [4, [5, [6, [7, 8, 9]]]]]]]

def flatten(arr):
    if not arr: return arr
    if isinstance(arr[0], list):
        return flatten(arr[0]) + flatten(arr[1:])
    return arr[:1] + flatten(arr[1:])
    
def depth(arr):
    if not arr: return 0
    if isinstance(arr, list):
        print('map', arr, *map(depth, arr))
        return 1 + max(map(depth, arr))
    else:
        return 0
    
print(flatten(arr))
print(depth(arr))
