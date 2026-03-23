a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
c=int(input("enter 3rd num:"))
if(a>b and a>c):
    print(a,"is greatest")
elif(b>c):
    print(b,"is greatest")
else:
    print(c,"is greatest")