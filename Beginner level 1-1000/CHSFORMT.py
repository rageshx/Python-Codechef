# cook your dish here
T=int(input())
for x in range(T):
    a,b=map(int,input().split())
    ans=a+b
    if(ans<3):
        print("1")
    elif(3<=ans and ans<=10):
        print("2")
    elif(11<=ans and ans<=60):
        print("3")
    else:
        print("4")
        
