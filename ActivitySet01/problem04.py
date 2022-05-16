a=float(input("Enter the hours"))
b=float(input("Enter the rate"))
if a<=40:
    c=a*b
else:
    c=(40*b)+((a-40)*b*1.5)        
print(c)    
    
    
