a= int(input("Enter a: "))
b= int(input("Enter b: "))
c= int(input("Enter c: "))
D= (b**2)-(4*a*c)
R1= (-b +(D**0.5))/2*a
R2= (-b -(D**0.5))/2*a
if D>0:
    print("Roots are", R1, R2)
else:
    print("It has no real roots")