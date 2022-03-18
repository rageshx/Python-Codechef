# cook your dish here
R=int(input())
for i in range(R):
    x=int(input())
    ans=x/4
    if(ans.is_integer()==True):
        print("Good")
    else:
        print("Not Good")
