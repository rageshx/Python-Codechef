# cook your dish here
T=int(input())
for i in range(T):
    (a,b,c,d)=map(int,input().split())
    opp1=a+c
    opp2=b+d
    if(opp1==opp2==180):
        print("YES")
    else:
        print("NO")
