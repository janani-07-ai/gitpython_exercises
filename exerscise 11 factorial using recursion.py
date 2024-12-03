# write a program to find factorial of using recursion function

def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("enter the number: "))
print("the factorial of number",n,"is",fact(n))
