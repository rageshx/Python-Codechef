# cook your dish here
R=int(input())
for i in range(R):
    (A,B,X,Y)=map(int,input().split())
    if((A*B)<=(X*Y)):
        print("Yes")
    else:
        print("No")
