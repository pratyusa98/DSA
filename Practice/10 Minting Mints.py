"""
Problem statement:

It was one of the places, where people need to get their provisions only through fair price (“ration”) shops.
 As the elder had domestic and official work to attend to, their wards were asked to buy the items from these shops.
  Needless to say, there was a long queue of boys and girls. To minimize the tedium of standing in the serpentine queue,
  the kids were given mints. I went to the last boy in the queue and asked him how many mints he has. He said that the
   number of mints he has is one less than the sum of all the mints of kids standing before him in the queue.
   So I went to the penultimate kid to know how many mints she has.



She said that if I add all the mints of kids before her and subtract one from it,
the result equals the mints she has. It seemed to be a uniform response from everyone.
So, I went to the boy at the head of the queue consoling myself that he would not give the same response as others.
He said, “I have four mints”.

Given the number of first kid’s mints (n) and the length (len) of the queue as input,
write a program to display the total number of mints with all the kids.
"""

s,n = map(int,input().split())
sum=s
for i in range(1,n):
    prev=sum-1
    sum+=prev
print(sum)