# write a program to find most frequent number from list

list=[2,3,4,5,2,4,2,5,2,8]
temp=0
count=0
index=0
for x in range(0,len(list)):
    temp= list.count(list[x])
    if temp>count:
        count=temp
        index=x
most_frequent=list[index]
print("The most frequent number is: ",most_frequent)
print("frequent in",count,"times in a list")




