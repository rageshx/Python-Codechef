# cook your dish here
T=int(input())
for i in range(T):
    (x,m,d)=map(int,input().split())
    ans1=(m*x)
    ans2=(x+d)
    ans=min(ans1,ans2)
    print(ans)
