# cook your dish here
T=int(input())
for i in range(T):
    (n,x,p)=map(int,input().split())
    crt=x*3
    incrt=(n-x)*-1
    total=crt+incrt
    if(total>=p):
        print("Pass")
    else:
        print("Fail")
