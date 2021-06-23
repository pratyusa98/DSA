
def longconsecutive(arr):
    arr = set(arr)
    longest = 0
    for i in arr:
        if i-1 not in arr:
            subsequence = 0
            while i in arr:
                i = i+1
                subsequence = subsequence +1
                longest = max(longest,subsequence)
    return longest



arr = [1,9,3,10,4,20,2]
print(longconsecutive(arr))