graph = {
    # 노드를 리스트로
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    # 간선을 리스트로 (weight, 각 끝점)
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (9, 'B', 'D'),
        (8, 'B', 'C'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (15, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (15, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


# 부모 노드 값 저장
parent = dict()
# 각각의 노드의 높이 번호
rank = dict()

def initialization(node):
    parent[node] = node
    rank[node] = 0

def find(node):
    # path compression
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_a, node_b):
    # union-by-rank
    root_a = find(node_a)
    root_b = find(node_b)

    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

        if rank[root_a] == rank[root_b]:
            rank[root_b] += 1

def kruskal(graph):
    mst = []

    # 초기화
    for node in graph['vertices']:
        initialization(node)
    # 간선을 오름차순으로 정렬
    edges = graph['edges']
    edges.sort()        #weight 기준으로 정렬

    # 사이클 확인 후 연결
    for edge in edges:
        weight, node_a, node_b = edge
        if find(node_a) != find(node_b):
            union(node_a, node_b)
            mst.append(edge)

    return mst

kruskal(graph)