# write a program to check number whether it is prime or not
a=int(input("Enter the number: "))
if a>1:
    for i in range(2,a): # we are not necessary to take 1 beacause we know 1 is not a prime no
        if a%i==0:
            print("the number",a," is not a prime number")
            break;
    else:
        print("the number",a,"is prime number")
else:
    print("the number is not a prime number")
