# cook your dish here
T=int(input())
for i in range(T):
    (x,y)=map(int,input().split())
    for j in range(y):
        if(x%2==0):
            x=x+1
        else:
            x=x-1
    if(x%2==0):
        print("Janmansh")
    else:
        print("Jay")
