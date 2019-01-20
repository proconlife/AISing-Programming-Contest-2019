n   = int(input())
a,b = map(int,input().split())
p   = map(int,input().split())
p_  = sorted(p)
 
anum = bnum = cnum = 0
for i,pi in enumerate(p_):
    if pi > a :
        anum = i
        break
 
for i,pi in enumerate(p_):
    if pi > b :
        bnum = i - anum
        break
 
cnum = n - anum - bnum
print(min(anum,bnum,cnum))
