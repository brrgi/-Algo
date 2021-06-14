import sys
input=sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

def dfs(node):
    # print("hi")
    visit[node] = True
    tree[node][0] = 0       #아닌 경우
    tree[node][1] = 1       #얼리어답터인 경우

    # print(tree)
    for i in link[node]:    #현재 노드와 연결된 노드들
        if visit[i]:        #방문했던 곳 제외
            continue
        dfs(i)
        tree[node][0] += tree[i][1]                     #현재 아닌 경우 += 자식 중에 얼리어답터 수
        tree[node][1] += min(tree[i][0], tree[i][1])    #현재 얼리어답터 += min(바로 밑 얼리어답터 자식의 얼리어답터 수
                                                        # , 바로 밑 얼리어답터 아닌 자식의 얼리어답터 수자식 중에 )


n = int(input())
link = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)

# print(tree)
tree = [[0, 0] for _ in range(n + 1)]

dfs(1)
print(min(tree[1][0], tree[1][1]))