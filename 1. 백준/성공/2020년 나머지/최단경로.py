# 5 6           v,e
# 1             k
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6
import sys
import heapq

input=sys.stdin.readline
INF=sys.maxsize
v,e=map(int,input().split())

k=int(input())

dp=[INF]*(v+1)
heap=[]
graph=[[] for _ in range(v+1)]

def dij(start):
    dp[start]=0
    heapq.heappush(heap,(0,start))
    
    while heap:
        weight, now=heapq.heappop(heap)
    
        for w, next_node in graph[now]:
            next_wei=weight+w
            if next_wei<dp[next_node]:
                dp[next_node]=next_wei
                heapq.heappush(heap, (next_wei,next_node))
                
for _ in range(e):
    u,v,w=map(int,input().split())
    graph[u].append((w,v))
    
dij(k)

for i in range(1,v+1):
    print("INF" if dp[i]==INF else dp[i])
