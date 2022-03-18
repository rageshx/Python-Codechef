# cook your dish here
R=int(input())
for i in range(R):
    (x1,y1,x2,y2)=map(int,input().split())
    part1=x1-x2
    part2=y1-y2
    if (part1<0):
        part1=part1*-1
    if(part2<0):
        part2=part2*-1
    ans=max(part1,part2)
    print(ans)
    
