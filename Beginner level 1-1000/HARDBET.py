# cook your dish here
t=int(input())
for i in range(t):
    (a,b,c)=map(int,input().split())
    if(a<b):
        if(a<c):
            print("Draw")
    if(b<a):
        if(b<c):
            print("Bob")
    if(c<a):
        if(c<b):
            print("Alice")
