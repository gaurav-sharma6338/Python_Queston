#WAP to Find it is armstrong number or not
n=153
arm=0
while(n!=0):
    r=n%10
    arm=arm**r
    n=n/10

if arm==n:
    print("It is a armstrong number")
else:
    print("It is not a armstrong number")