leng = int(input(" "))
m=leng-1
for i in range(0,leng):
    for j in range(0,m):
        print(" ",end = "")
    for k in range(0,i+1):
        print("*",end = "")
    m=m-1
    print("")
m=leng-1
for n in range(1,leng+1):
    for o in range(0,n):
        print(" ",end = "")
    for p in range(0,m):
        print("*",end = "")
    m=m-1
    print("")
