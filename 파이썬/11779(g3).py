import heapq
import sys
input=sys.stdin.readline

V=int(input())
E=int(input())

INF=sys.maxsize
distance=[[] for _ in range(V+1)]
prev=[-1 for _ in range(V+1)]
for _ in range(E):
    start, end, dist=map(int, input().split())
    distance[start].append([end,dist])
K, goal=map(int,input().split())

def dijkstra():
    global K_distance, end, prev

    queue = []
    K_distance = [INF for _ in range(V + 1)]
    K_distance[K] = 0  # 자기자신
    heapq.heappush(queue, [0, K])  # 자기 자신이 우선순위 큐      [거리, 정점]
    while queue:
        mid = heapq.heappop(queue)
        for end in distance[mid[1]]:
            if K_distance[end[0]] > mid[0] + end[1]:
                K_distance[end[0]] = mid[0] + end[1]
                prev[end[0]]=mid[1]
                heapq.heappush(queue, [K_distance[end[0]], end[0]])

dijkstra()

K_distance.pop(0)
prev.pop(0)

# costResult, p =