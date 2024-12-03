# write a program to find hcf
a= int(input("ENTER THE NUMBER a: "))
b=int(input("ENTER THE NUMBER b: "))
if a>b:
    min = a
else:
    min = b
while(True):
    if min%a==0 and min%b==0:
        HCF = min
        break;
    min-=1
print(HCF)

