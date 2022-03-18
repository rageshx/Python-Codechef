# cook your dish here
T=int(input())
for i in range(T):
    (X,Y,Z)=map(int,input().split())
    if(((Z*2)+X>=Y) or ((Z*1)+X>=Y)):
        print("YES")
    else:
        print("NO")
        
