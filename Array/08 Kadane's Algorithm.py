
"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
"""


def maxSubArraySum(a, n):
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, n):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)

    return max_so_far

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(maxSubArraySum(arr, len(arr)))