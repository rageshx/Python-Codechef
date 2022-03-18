# cook your dish here
(R,O,C)=map(int,input().split())
rem=20-O
Bplay=rem*6
Bscore=Bplay*6
Btotal=C+Bscore
if(Btotal>R):
    print("Yes")
else:
    print("No")
