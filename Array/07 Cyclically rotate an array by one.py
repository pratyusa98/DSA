
def rotate(arr,n):
    a = arr[n-1]
    for i in range(n-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = a
    return arr

arr= [1,2,3,4,5,6]
n = len(arr)
print(rotate(arr,n))