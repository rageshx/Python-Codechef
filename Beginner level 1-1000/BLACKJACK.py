# cook your dish here
R=int(input())
for i in range(R):
    (a,b)=map(int,input().split())
    sum1=a+b
    for j in range(0,11):
        if (sum1+j==21):
            print(j)
            break
    else:
        print("-1")
        
        
