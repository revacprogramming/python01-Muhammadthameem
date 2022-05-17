def computepay(a,b):
    if a<=40:
        c=a*b
    else:
        c=(40*b)+((a-40)*b*1.5)
    return c
a=float(input("Enter hours"))
b=float(input("Enter rate"))
c=computepay(a,b)
print("Pay "+str(c))
    
