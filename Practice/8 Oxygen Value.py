"""
The selection of MPCS exams includes a fitness test which is conducted on the ground.
There will be a batch of 3 trainees, appearing for a running test on track for 3 rounds.

You need to record their oxygen level after every round.
After trainees are finished with all rounds, calculate for each trainee his average oxygen
level over the 3 rounds and select the one with the highest average oxygen level as the fittest trainee.
If more than one trainee attains the same highest average level, they all need to be selected. Display the
fittest trainee(or trainers) and the highest average oxygen level.
"""

T1 = int(0)
T2 = int(0)
T3 = int(0)
count = int(0)
while(count<9):
    x=int(input())
    if(x>=1 and x<=100):
        if(count%3==1):
            T1=T1+x
        elif(count%3==2):
            T2=T2+x
        else:
            T3=T3+x
        count=count+1
    else:
        print("INVALID INPUT")
        exit()
A1 = round(T1/3)
A2 = round(T2/3)
A3 = round(T3/3)
print(A1,A2,A3)
if(A1 <= 70 and A2 <= 70 and A3 <= 70):
    print("All trainees are unfit")
    exit()
if(A1 >= A2 and A1>= A3):
    print("Trainee Number: 1")
if(A2 >= A1 and A2 >= A3):
    print("Trainee Number: 2")
if(A3 >= A1 and A3 >= A2):
    print("Trainee Number: 3")