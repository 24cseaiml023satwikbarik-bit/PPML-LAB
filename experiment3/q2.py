import math
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))
d=b*b-4*a*c
if d>0:
    r1=(-b+math.sqrt(d)/2*a)
    r2=(-b-math.sqrt(d)/2*a)
    print("two real roots:",r1,r2)
elif d==0:
    r=-b/(2*a)
else:
    print("no real roots")