"""
Given an array arr[] and a number K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
 It is given that all array elements are distinct.
"""

def klarge(arr,k):
    arr.sort(reverse=True)
    return arr[k-1]

def ksmall(arr,k):
    arr.sort()
    return arr[k-1]

arr = [7,10,4,3,20,15]
k = 2
print(k,"th Smallest Element is: ",ksmall(arr,k))
print(k,"th Largest Element is: ",klarge(arr,k))