# cook your dish here
t=int(input())
for i in range(t):
    z,y,a,b,c=[int(x) for x in input().split()]
    rem=z-y
    games=a+b+c
    if(rem>=games):
        print("YES")
    else:
        print("NO")
