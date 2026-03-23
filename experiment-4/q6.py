n=int(input("enter a non negative integer:"))
if n<0:
    print("not possible")
else:
    fact=1
    i=1
    while i<=n:
        fact*=i
        i+=1
print("factorial:",fact)