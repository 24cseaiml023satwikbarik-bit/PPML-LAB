l=[]
n=int(input("no. of terms:"))
for i in range(n):
    l.append(int(input()))
res=sorted(list(set(l)))
print("sorted:",res)
