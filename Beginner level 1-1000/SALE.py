# cook your dish here
T=int(input())
for i in range(T):
    a = list(map(int, input().split()))
    a.remove(min(a))
    print(sum(a))
