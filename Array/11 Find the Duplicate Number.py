
def duplicate(arr):
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return arr[j]


arr = [1,2,2,3]
print(duplicate(arr))
