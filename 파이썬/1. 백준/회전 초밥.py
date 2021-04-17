N,d,k,c=map(int,input().split(" "))
s=[]
for _ in range(N):
    b=int(input())
    s.append(b)

maxs=0
for x in range(N):
    y=[]
    t=x
    for _ in range(k):
        if t+1==N:
            t=-1
        y.append(s[t+1])
        t+=1
    y.append(c)
    sety=set(y)
    if len(sety)>maxs:
        maxs=len(sety)
print(maxs)