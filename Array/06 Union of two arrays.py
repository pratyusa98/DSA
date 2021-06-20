
arr1 = [1,2,3,4,5]
arr2 = [1,2,3]

A=len(set(arr1)|set(arr2))
B=len(set(arr1)&set(arr2))

print('Union of the arrays:',A)
print('intersection of the arrays:',B)