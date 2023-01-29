#diamond star pattern :)
n=int(input(" "))
for a in range(1,n+1):
    for i in range(a-1,n-1):
        print(" ",end = "")
    for j in range(0,a):
        print("*",end=" ")
    print("")
for x in range(1,n):
    for b in range(0,x):
        print(" ",end="")
    for c in range(x,n):
        print("*",end=" ")
    print("")
