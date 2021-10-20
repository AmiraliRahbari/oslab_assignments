a=int(input("please enter a number:"))
for i in range(1,a):
    f=1
    flag=0
    for j in range(1,i+1):
        f=f*j
    if a==f:
        print("yes")
        flag=1
        break

if flag==0:
    print("no")
