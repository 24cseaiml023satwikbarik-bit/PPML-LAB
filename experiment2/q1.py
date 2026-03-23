p=int(input("enter the principle:"))
t=int(input("enter time in years:"))
r=float(input('enter rate of interest:'))
n=int(input("enter no. of times compunded yearly:"))
si=(p*t*r)/100
ci=((1+(r/n))**(n*t))
print("SI:",si,"\nCI:",ci)
