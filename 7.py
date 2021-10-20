n=int(input("please a number:"))
m=int(input("please a number:"))
for i in range(0,m+n):
    r=m%n
    if r==0:
        break
    m=n
    n=r
print("BMM:"+str(n))
