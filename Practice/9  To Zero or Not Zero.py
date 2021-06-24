"""
Given a pair of positive integers m and n (m < n; 0 < m < 999; 1 < n < = 999),
write a program to smartly affix zeroes, while printing the numbers from m to n.

Input

5 10

Expected output

05 06 07 08 09 10

"""

start = int(input())
end = int(input())
n = len(str(end))
for i in range(start,end+1):
    if end >= 100:
        print("{:03d}".format(i),end=" ")
    elif end >= 10:
        print("{:02d}".format(i), end=" ")
    else:
        print(i,end=" ")