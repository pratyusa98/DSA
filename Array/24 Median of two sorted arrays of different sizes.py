import math
def mediandiff(ar1,ar2):
    arr = ar1+ar2
    arr.sort()

    n = len(arr)
    if n % 2 != 0:
        result = (math.ceil(n/2))-1
        return arr[result]

    else:
        index1 =  arr[math.ceil(n/2)]
        index2 = arr[math.ceil(n/2)-1]
        result = math.floor((index1+index2)/2)
        return result

ar1 = [900]
ar2 = [5, 8, 10, 20]
print(mediandiff(ar1,ar2))