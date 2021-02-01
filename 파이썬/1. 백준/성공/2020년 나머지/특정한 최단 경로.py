import heapq
import sys
input=sys.stdin.readline
INF=sys.maxsize

n,m=map(int,input().split())  #x는 목적지
distance=[[] for _ in range(n+1)]
for i in range(m):
    start, end, dist=map(int,input().split())
    distance[start].append([end, dist])
    distance[end].append([start,dist])
v1,v2=map(int,input().split())

def dijkstra(start, goal, past):
    queue=[]
    n_distance=[INF for _ in range(n+1)]
    n_distance[start]=past             #자기자신
    heapq.heappush(queue,[past,start]) #[거리, 정점]
    while queue:
        mid=heapq.heappop(queue)        #mid[1]은 정점
        for end in distance[mid[1]]:
            if n_distance[end[0]]>mid[0]+end[1]:
                n_distance[end[0]]=mid[0]+end[1]
                heapq.heappush(queue, [n_distance[end[0]], end[0]])
    return n_distance[goal]

result=[]
first=dijkstra(1, v1, 0)
second=dijkstra(1, v2, 0)
one_two=INF
two_one=INF
result1=INF
result2=INF
toggle=0
if first!=INF:
    one_two=dijkstra(v1,v2,first)
if second!=INF:
    two_one=dijkstra(v2,v1,second)
if first==INF and second==INF:
    toggle=1

if one_two!=INF:
    result1=dijkstra(v2,n,one_two)
if two_one!=INF:
    result2=dijkstra(v1,n,two_one)
if one_two==INF and two_one==INF:
    toggle=1
if result1==INF and result2==INF:
    toggle=1

if toggle==1:
    print(-1)
else:
    print(min(result1, result2))
