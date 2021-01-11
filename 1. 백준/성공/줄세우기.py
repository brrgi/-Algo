a=int(input())
t=[]
for i in range(a):
    c=int(input())
    t.append(c)

dp=[0 for i in range(a)]

for i in range(1,a):
    for j in range(i):
        if t[i]>t[j]:
            if dp[i]<dp[j]+1:
                dp[i]=dp[j]+1

print(a-max(dp)-1)
