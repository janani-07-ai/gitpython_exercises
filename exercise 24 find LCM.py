# write a program to find LCM

n1= int(input("ENTER THE NUMBER N1: "))
n2= int(input("ENTER THE NUMBER N2: "))
if n1>n2:
    max=n1
else:
    max=n2
while(True):
    if max%n1==0 and max%n2==0:
        lcm = max
        break
    max+=1
print(lcm)