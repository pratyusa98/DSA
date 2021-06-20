"""
Common Elements in Three Array
"""

def commonele(A,B,C):
    common = list(set(A) & set(B) & set(C))
    return common


arr1 = [1,2,3,4,5]
arr2 = [2,3,4,6,9,8]
arr3 = [2,3,6]

print(commonele(arr1,arr2,arr3))