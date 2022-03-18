# cook your dish here
t=int(input())
for i in range(t):
    xa,xb,Xa,Xb=map(int,input().split())
    a1=Xa/xa
    a2=Xb/xb
    print(int(a1+a2))
