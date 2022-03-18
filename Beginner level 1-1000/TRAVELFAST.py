# cook your dish here
R=int(input())
for i in range(R):
    (x,y)=map(int,input().split(" "))
    if (x==y):
        print("SAME")
    elif(x<y):
        print("BIKE")
    else:
        print("CAR")
