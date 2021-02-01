import sys
input=sys.stdin.readline

a=int(input())

k=list(map(int,input().split()))

dp=[1 for i in range(a)]
dp2=[1 for i in range(a)]
dp3=[0 for i in range(a)]
for i in range(1, a):
    for j in range(i):
        if k[i]>k[j]:
            dp[i]=max(dp[i], dp[j]+1)

for i in range(a-2, -1, -1):
    for j in range(a-1, i,-1):
        if k[i]>k[j]:
            dp2[i]=max(dp2[i], dp2[j]+1)

for i in range(a):
    dp3[i]=dp[i]+dp2[i]-1
print(max(dp3))
