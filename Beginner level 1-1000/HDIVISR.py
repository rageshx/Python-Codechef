# cook your dish here
t=int(input())
l=[]
for i in range(1,11):
    if(t%i==0):
        l.append(i)
print(max(l))
        
