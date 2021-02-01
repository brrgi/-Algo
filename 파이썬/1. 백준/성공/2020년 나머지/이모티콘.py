from collections import deque
s=int(input())
dp=[[-1 for i in range(1001)] for i in range(1001)]

queue=deque()
queue.append([1,0]) #화면, 클립보드, 현재까지 소요 시간

dp[1][0]=0
while queue:
    screen, clipboard=queue.popleft()

    if dp[screen][screen]==-1:
        dp[screen][screen]=dp[screen][clipboard]+1
        queue.append([screen, screen])

    if screen+clipboard<=s and dp[screen+clipboard][clipboard]==-1:
        dp[screen+clipboard][clipboard]=dp[screen][clipboard]+1
        queue.append([screen+clipboard,clipboard])
    if screen>=1:
        if dp[screen-1][clipboard]==-1:
            dp[screen-1][clipboard]=dp[screen][clipboard]+1
            queue.append([screen-1, clipboard])
result=-1
for i in range(s):
    if dp[s][i]!=-1:
        if result==-1:
            result=dp[s][i]
        elif result>dp[s][i]:
            result=dp[s][i]
print(result)
