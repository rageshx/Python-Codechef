# cook your dish here
T=int(input())
for x in range(T):
    (a,b)=map(int,input().split())
    if(a>0 and b>0):
        print("Solution")
    else:
        if(a==0):
            print("Liquid")
           
        if(b==0):
            print("Solid")
            
            
           
