# cook your dish here
t=int(input())
for i in range(t):
    (m,n,k)=map(int,input().split())
    time=n*k
    if(time<m):
        print("YES")
    else:
        print("NO")
