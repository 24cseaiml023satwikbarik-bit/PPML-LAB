l=['mango','apple','banana','cherry','pineapple']
li=[]
for i in range(len(l)-1,0,-1):
    print(l[i]," len=",len(l[i]))
    li.append(l[i][::-1])

print(li)