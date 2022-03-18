# cook your dish here
R=int(input())
for i in range(R):
    (X,A,B)=map(int,input().split())
    mark1=A*1
    mark2=B*2
    ans=mark1+mark2
    if(X<=ans):
        print("Qualify")
    else:
        print("NotQualify")
