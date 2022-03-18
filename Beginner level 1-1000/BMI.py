# cook your dish here
t=int(input())
for i in range(t):
    m,h=map(int,input().split())
    h2=h**2
    ans=m/h2
    if(ans<=18):
        print("1")
    elif(ans>=30):
        print("4")
    elif(ans in [19,20,21,22,23,24]):
        print("2")
    else:
        print("3")
