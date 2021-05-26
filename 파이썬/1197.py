from collections import defaultdict
from heapq import *


def prim(adjacent_edges, start_node):
    value = 0
    visit[start_node] = 1
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if visit[n2] == 0:
            visit[n2] = 1
            value += weight

            for edge in adjacent_edges[n2]:  # weight, n1, <n2>~~
                if visit[edge[2]] == 0:
                    heappush(candidate_edge_list, edge)
    return value


v, e = map(int, input().split())
adjacent_edges = defaultdict(list)
visit = [0 for _ in range(v + 1)]
for i in range(e):
    u, v, weight = map(int, input().split())
    adjacent_edges[u].append([weight, u, v])
    adjacent_edges[v].append([weight, v, u])
print(prim(adjacent_edges,1))  # start_node, myedges
# (7 , 'A', 'b') 가중치,
