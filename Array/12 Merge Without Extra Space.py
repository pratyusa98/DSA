

def merge(a,b):
    c = a+b
    c.sort()
    return c

arr1 = [1,3,5,7]
arr2 = [0, 2, 6, 8, 9]
print(merge(arr1,arr2))