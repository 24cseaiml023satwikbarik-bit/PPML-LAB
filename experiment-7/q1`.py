m=-int(input("enter the starting of the natural number:"))
n=int(input("enter the ending of the natural number:"))
l=[x for x in range(m,n+1)]
print("the sum of the list is:",sum(l))
print("the average of in the list is:",(sum(l)/len(l)))
print("the largest element element in the list is:",max(l))
print("the smallest element in the list is:",min(l))
l2=[x for x in l if x%3!=0]
print("the elements which are not divisible by 3 are:",l2)
