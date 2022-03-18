# cook your dish here
T=int(input())
for x in range(T):
    (x,y)=map(int,input().split())
    print(min(x//2,y))
    
