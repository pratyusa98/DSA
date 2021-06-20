
def recur_factorial(n):
    # if n == 1:
    #    return n
    # elif n < 1:
    #    return ("NA")
    # else:
    #    return n*recur_factorial(n-1)
    return 1 if (n == 1 or n == 0) else n * recur_factorial(n - 1);


num = int(input("Enter a number: "))
print(recur_factorial(num))