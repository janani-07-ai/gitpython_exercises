# write a program to find factorial of using for loop

n=int(input("enter the number: "))
result=1
for i in range(n,0,-1):
    result=result*i
print("factorial of number" ,n, "is",result)