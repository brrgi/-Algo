import heapq
import sys
input=sys.stdin.readline
INF=sys.maxsize

n,m,x=map(int,input().split())  #x는 목적지
distance=[[] for _ in range(n+1)]

for i in range(m):
    start, end, dist=map(int,input().split())
    distance[start].append([end, dist])

def dijkstra(start, goal):
    queue=[]
    n_distance=[INF for _ in range(n+1)]
    n_distance[start]=0       #자기자신
    heapq.heappush(queue,[0,start]) #[거리, 정점]
    while queue:
        mid=heapq.heappop(queue)        #mid[1]은 정점
        for end in distance[mid[1]]:
            if n_distance[end[0]]>mid[0]+end[1]:
                n_distance[end[0]]=mid[0]+end[1]
                heapq.heappush(queue, [n_distance[end[0]], end[0]])
    return n_distance[goal]

result=[]
for i in range(1, n+1):
    if i==x:
        continue
    go=dijkstra(i, x)
    back=dijkstra(x, i)
    if go!=INF and back!=INF:
        result.append(go+back)
print(max(result))
