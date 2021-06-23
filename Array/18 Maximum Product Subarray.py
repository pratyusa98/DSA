"""
Input: arr[] = {6, -3, -10, 0, 2}
Output:   180  // The subarray is {6, -3, -10}

Input: arr[] = {-1, -3, -10, 0, 60}
Output:   60  // The subarray is {60}

Input: arr[] = {-2, -40, 0, -2, -3}
Output:   80  // The subarray is {-2, -40}
"""


def maxproduct(arr,n):
    max_end = 1
    min_end = 1

    max_far = 0
    flag = 0

    for i in range(0,n):
        #positive
        if arr[i]>0:
            max_end = max_end*arr[i]
            min_end = min(min_end*arr[i],1)
            flag = 1
        #zero
        elif arr[i] == 0:
            max_end = 1
            min_end = 1

        #negative
        else:
            temp = max_end
            max_end = max(min_end*arr[i],1)
            min_end = temp*arr[i]

        if max_far < max_end:
            max_far = max_end
    if flag == 0 and max_far == 0 :
        return 0
    return max_far


arr = [-2, -40, 0, -2, -3]
n = len(arr)
print(maxproduct(arr,n))