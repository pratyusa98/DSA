"""
There is a jar full of candies for sale at a mall counter.
The jar has the capacity N, that is JAR can contain maximum N Candies when a JAR is full.
At any point in time, JAR can have an M number of candies where M<=N. Candies are served to the customers.
JAR is never remaining empty as when the last K candidates are left, JAR is refilled with new candidates
in such a way that JAR gets full.

Write the code to implement the above scenario. Display JAR at the
counter with the available number of candies.

Input should be the number of candies one customer orders at a point in time.
Update the JAR after every purchase and display JAR at the counter. The output should give the number
of candies sold and the updated number of candies in the JAR. If the input is more
than the number of candies in JAR, return “INVALID INPUT”.

Input #1:
3
Output :
Number of Candies Sold: 3
Number of Candies available:7

"""

n=int(10)
k=int(input())
if(k==0):
    print("INVALID INPUT")
    print("NUMBER OF CANDIES AVAILABLE: ",n)
else:
    print("NUMBER OF CANDIES SOLD: ",k)
    print("NUMBER OF CANDIES AVAILABLE: ",n-k)