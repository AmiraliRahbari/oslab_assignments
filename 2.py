from random import randint
n=int(input("please enter n:"))
arr=[]
arr.append(randint(0,100))
for i in range(1,n):
    flag=1
    a=randint(0,100)
    for j in range(0,i):
        if a==arr[j]:
            flag=0
    if flag==1:
       arr.append(a)
    else:
        i=i-1
       
    
print(arr)
