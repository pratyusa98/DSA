"""
Write a code to check whether no is prime or not. Condition use function check()
to find whether entered no is positive or negative ,if negative then enter the no,
 And if yes pas no as a parameter to prime() and check whether no is prime or not?

"""
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

else:
    print(num)