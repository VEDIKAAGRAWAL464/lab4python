#Take 3 variables
X= int(input("Enter X: "))
Y= int(input("Enter Y: "))
N = int(input("Enter N: "))
while X<Y: #Work till X is less than Y
    X= X+1
    if X%N==0:   #check if X is divisible by N
        print(X)
