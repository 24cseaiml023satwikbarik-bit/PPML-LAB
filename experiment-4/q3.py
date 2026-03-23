a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
while(b!=0):
    temp=a
    a=b
    b=temp%b
while c!=0:
    temp=a
    a=c
    c=temp%c
print("gcd:",a)
