# patter Y 1
n = int(input(""))
while(n%2==0):
    n=int(input("even numers aren't allowed retry: "))
print("ok")
front = round(n/2.1)
print(front)
x,y=1,n
for a in range(1,front+1):
    for i in range(1,n+1):
        if(i==x or i ==y):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    x+=1
    y-=1
for f in range(0,front):
    for g in range(1,front+2):  #changes made here and next line
        if(g==front+1):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    front-=1
