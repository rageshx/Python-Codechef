# cook your dish here
t=int(input())
for i in range(t):
    s=input()
    t=input()
    ans=""
    for j in range(5):
        if(s[j]==t[j]):
            ans+="G"
        else:
            ans+="B"
    print(ans)
