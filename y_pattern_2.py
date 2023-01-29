#perfect pattern Y 2
n = int(input(""))
while(n%2==0):
    n=int(input("even numers aren't allowed retry: "))
print("ok")
if(n<=35):
    front = round(n/1.9) # was able to escalate imerfect y on no 35 and below
else:
    front = round(n/2) # same escalation with no 39 and above 
    print(front)
x,y=1,n
for a in range(1,front+1):
    if(a==front):            #changes made here and next line.
        break
    for i in range(1,n+1):
        if(i==x or i ==y):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    x+=1
    y-=1
for f in range(0,front):
    for g in range(1,front+1):
        if(g==front):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
    front-=1
