# cook your dish here
T=int(input())
for i in range(T):
    x=int(input())
    bags=0
    temp=0
    if(x%10==0):
        print(x//10)
    else:
        bags=x//10
        temp=x%10
        if(temp>0):
            bags=bags+1
            print(bags)
        
