
## Check all element in array palindrome Or not

def isPalindrome(N):
    str1 = "" + str(N)
    len1 = len(str1)
    for i in range(int(len1 / 2)):
        if (str1[i] != str1[len1 - 1 - i]):
            return False
    return True


def isPalinArray(arr, n):
    for i in range(n):
        ans = isPalindrome(arr[i])
        if (ans == False):
            return False
    return True



arr = [121,131,20]

# length of array
n = len(arr)
res = isPalinArray(arr, n)
if (res == True):
    print("Array is a PalinArray")
else:
    print("Array is not a PalinArray")


