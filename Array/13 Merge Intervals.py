
def mergeIntervals(arr):
    arr.sort(key=lambda x: x[0])

    m = []
    s = -10000
    max = -100000
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i != 0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]


    if max != -100000 and [s, max] not in m:
        m.append([s, max])
    for i in range(len(m)):
        print(m[i], end=" ")


# Driver code
arr = [[1,3],[2,6],[8,10],[15,18]]
mergeIntervals(arr)
