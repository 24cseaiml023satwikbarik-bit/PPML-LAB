dic=dict()
n=int(input("enter number of elements:"))
for i in range(n):
    key=input("enter key:")
    val=input("enter val:")
    dic[key]=val
dict=dict()
for (i,j) in (dic.keys(),dic.values()):
    dict[j]=i
print("dic1:",dic)
print("dic2:",dict)
