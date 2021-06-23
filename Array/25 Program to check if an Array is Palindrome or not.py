
def isPalindrome(arr,n):
    for i in range(0, int(n/2)):
        if arr[i] != arr[n - 1 - i]:
            return 'Array Is Not Palindrome'

    return 'Array Is Palindrome'


arr = [15, 4, 15]
n = len(arr)
print(isPalindrome(arr,n))