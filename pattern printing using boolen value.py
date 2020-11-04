print("entered value of n(number of rows)")
n=int(input())
print("enter the bool value")
a=int(input())
if(a==1):
 for i in range(1,n):
    for j in range(1,i+1):
        print("*",end="")
    print()
elif(a==0):
 for i in range(1,n):
    for j in range(n,i,-1):
        print("*",end="")
    print()
else:
    print("invalide input")
    
