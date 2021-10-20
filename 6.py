n=int(input("please enter size of array:"))
arr=[]
for i in range(0,n):
    a=int(input("please enter num:"))
    arr.append(a)
flag=1
for i in range(0,n-1):
    if arr[i]>arr[i+1]:
        flag=0
        break
if flag==1:
    print("yes")
else:
    print("no")
