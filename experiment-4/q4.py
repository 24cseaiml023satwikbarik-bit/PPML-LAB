n=int(input("enter a positive integer:"))
sum=0
while n>0:
    sum+=n%10
    n//=10
print("sum of digits:",sum)
