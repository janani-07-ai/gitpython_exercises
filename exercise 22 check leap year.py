# write a program to check leap year

a= int(input("Enter the year:"))
if a%4==0 and (a%100!=0 or a%400==0):
    print("The year is leap year")
else:
    print("THe year is not a leap year")

