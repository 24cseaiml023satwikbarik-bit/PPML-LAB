str=input("enter sentence:")
l1=str.split(" ")
for i,j in enumerate(l1):
    print(i,j)
l2=[i for i in range(len(l1))]
print(l2)
l3=list(zip(l1,l2))
print(l3)