# cook your dish here
n=int(input())
for i in range(n):
    x=int(input())
    l=[int(x) for x in input().split()]
    count=0
    for i in l:
        if i>=10 and i<=60:
            count+=1
    print(count)
