a=int(input("please enter a num:"))
b=a
count=0
summ=0
while b!=0:
    b=b//10
    count=count+1
b=a
while b!=0:
    r=b%10
    summ=summ+r**count
    b=b//10
if a==summ:
    print("yes")
else:
    print("no")
    
