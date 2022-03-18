# cook your dish here
T=int(input())
for x in range(T):
    l=[int(x) for x in input().split()]
    s=0
    r=0
    for i in l:
        if(i==1):
            s=s+1
        else:
            r=r+1
    if(s>r):
        print("Yes")
    else:
        print("No")
