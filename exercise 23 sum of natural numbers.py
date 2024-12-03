# write a program to find sum of natural numbers
a= int(input("enter the number: "))
sum_of_natural_numbers=sum(i for i in range(1,a+1)) # generator method
print("sum: ",sum_of_natural_numbers)

# using formulae

a= int(input("enter the number: "))
sum_of_natural_numbers= a*(a+1)//2
print("sum: ",sum_of_natural_numbers)
