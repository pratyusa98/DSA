
# O(n2)
# def traprain(arr,n):
#
#     res = 0
#     for i in range(1,n-1):
#         left = arr[i]
#         for j in range(i):
#             left = max(left,arr[j])
#
#
#         right = arr[i]
#         for j in range(i+1,n):
#             right = max(right,arr[j])
#
#         res = res + (min(left,right)-arr[i])
#
#     return res
#
#
#
# arr = [6,9,9]
# n = len(arr)
# print(traprain(arr,n))

#O(n)

# Python program to find maximum amount of water that can
# be trapped within given set of bars.

def findWater(arr, n):
    left = [0]*n
    right = [0]*n

    water = 0

    left[0] = arr[0]
    for i in range( 1, n):
        left[i] = max(left[i-1], arr[i])

    right[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        right[i] = max(right[i + 1], arr[i]);

    for i in range(0, n):
        water += min(left[i], right[i]) - arr[i]

    return water



arr = [3,0,0,2,0,4]
n = len(arr)
print(findWater(arr, n))

