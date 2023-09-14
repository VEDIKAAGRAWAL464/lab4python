n= int(input("Enter any number: "))
i=1
if n<0 or n==0:
    print("Input is invalid")
else:
    while i<21:
        print(n,"x",i,"=", i*n)
        i= i+1
    