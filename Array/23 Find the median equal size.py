import math
def median(arr,n):
    
    arr.sort()
    if n % 2 != 0:
        result = (math.ceil(n/2))-1
        return arr[result]

    else:
        index1 =  arr[math.ceil(n/2)]
        index2 = arr[math.ceil(n/2)-1]
        result = math.floor((index1+index2)/2)
        return result


arr = [2,5,4,3,50,60]
n = len(arr)
print(median(arr,n))