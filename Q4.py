#WAP to find factorial
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)

#driver code
result=factorial(5)
print("The factorial is ",result)