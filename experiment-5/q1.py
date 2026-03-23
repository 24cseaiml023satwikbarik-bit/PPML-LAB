a=0
b=1
for i in range(1000):
    if a>1000:
        break
    print(a,end=",")
    if a%2==0:
        sum+=a
    temp=a
    a=b
    b=temp+b
print("sum=",sum)
