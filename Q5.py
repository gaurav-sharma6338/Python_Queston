#WAP to find Compund Interest
P=int(input("Enter principal value:-"))
r=int(input("Enter interst rate:-"))
n=int(input("Enter Number of times interest is compounded per year:-"))
t=int(input("Enter year:-"))
A = P * (1 + r/n)**(n*t)

print("You Compound interest is ",A)