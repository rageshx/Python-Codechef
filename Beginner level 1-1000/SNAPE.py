# cook your dish here
T=int(input())
for i in range(T):
    b,ls=map(int,input().split())
    b2=b**2
    ls2=ls**2
    ans1=float((ls2-b2)**0.5)
    ans2=(ls2+b2)**0.5
    print(format(ans1,".4f"),format(ans2,".4f"))
