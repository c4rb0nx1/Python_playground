n=int(input(""))
m=n-1
for i in range(1,n+1):
    print("*",end=" ")
print("")
for a in range(0,m):
    for k in range(0,n+1):
        if(k==0 or k==n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
for x in range(1,n+1):
    print("*",end=" ")
print("")
