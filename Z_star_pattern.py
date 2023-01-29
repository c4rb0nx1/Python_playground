# z pattern in python
n=int(input(""))
for i in range(0,n):
    print("*",end=" ")
print("")
for j in range(1,n-1):
    for a in range(j,n-1):
        print(" ",end =" ")
    print("*")
for x in range(0,n):
    print("*",end=" ")
