n = int(input(" "))
for i in range(0,n+1):
    for j in range(0,i):
        print("*",end = "")
    print("")
p=n-1
for k in range(0,n-1):
    for h in range(0,p):
        print("*",end = "")
    print("")
    p-=1
