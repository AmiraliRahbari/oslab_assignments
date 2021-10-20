n=int(input("please a number:"))
m=int(input("please a number:"))
a=n
b=m
for i in range(0,m+n):
    r=m%n
    if r==0:
        break
    m=n
    n=r
k=(a*b)/n
print("KMM:"+str(k))
