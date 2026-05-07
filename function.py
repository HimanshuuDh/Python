def max( a,b,c):
   
    if a>b and a>c:
      d=a
    elif b>a and b>c:
        d=b
    else:
       d=c
    return d


a=float(input("Enter the value of a: "))
b=float(input("Enter the value of b: "))
c=float(input("Enter the value of c: "))

result= max(a,b,c)
print("The largest number is ",result)



