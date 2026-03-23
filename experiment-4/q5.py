n=int(input("enter an integer:"))
original=n
reverse=0
while n>0:
    digits=n%10
    reverse=reverse*10+digits
    n//=10
if original==reverse:
    print("palindrome")
else:
    print("not paloindrome")

