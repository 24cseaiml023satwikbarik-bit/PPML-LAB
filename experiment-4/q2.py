import math
n=int(input("enter a number:"))
if n<=1:
    print(f"{n} is not a prime")
else:
    i=2
    while i<=math.sqrt(n):
        if n%i==0:
            print(f"{n} is not a prime")
            break
        i+=1
    else:
        print(f"{n} is a prime")