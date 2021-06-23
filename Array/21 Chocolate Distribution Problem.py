

def chocolate(arr,N,M):

    #no chocolate and student 0
    if (N==0 or M==0):
        return 0

    # sort array
    arr.sort()

    #no of student cant be more than no of packet

    if(N < M):
        return -1

    min_diff = arr[N-1] - arr[0]

    for i in range(len(arr)-M+1):
        min_diff = min(min_diff,arr[i+M-1]-arr[i])

    return min_diff


arr = [7, 3, 2, 4, 9, 12, 56]
M = 3
N = len(arr)
print(chocolate(arr,N,M))