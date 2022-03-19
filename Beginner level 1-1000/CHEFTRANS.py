# cook your dish here
t=int(input())
for i in range(t):
    (x,y,z)=map(int,input().split())
    s=x+y
    if(s<z):
        print("Planebus")
    if(s==z):
        print("EQUAL")
    if(s>z):
        print("Train")
