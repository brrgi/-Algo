from collections import deque
n=int(input())
k=[0 for i in range(1001)]
t=input().split()
for i in range(n):
    k[i]=int(t[i])

dp=[[1,-1] for i in range(1001)]
dp[0][0]=1

for i in range(1,1001):
    for j in range(0, i):
        if k[j]<k[i]:
            if dp[i][0]<dp[j][0]+1:
                dp[i][0]=dp[j][0]+1
                dp[i][1]=j

sth = max(dp, key=lambda x: x[0])
now = dp.index(sth)

a=deque()
a.append(k[now])
now=sth[1]
for i in range(sth[0]-1):
    a.appendleft(k[now])
    now=dp[now][1]

print(sth[0])
print(*a)
