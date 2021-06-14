import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def dfs(node):
    # print("hi")
    visit[node] = True
    tree[node][0] = people[node-1]        #우수마을인 경우

    # print(tree)
    for i in link[node]:    #현재 노드와 연결된 노드들
        if not visit[i]:        #방문했던 곳 제외
            dfs(i)
            tree[node][0] += tree[i][1]                     #현재 우수마을 ㅇ
            tree[node][1] += max(tree[i][0], tree[i][1])    #현재 우수마을  X



n = int(input())
people = list(map(int, input().split()))
link = [[] for _ in range(n + 1)]   #0번째 인덱스 사용 x
visit = [False] * (n + 1)
for _ in range(n - 1):
    u, v = map(int, input().split())
    link[u].append(v)
    link[v].append(u)


# print(tree)
tree = [[0, 0] for _ in range(n + 1)]

dfs(1)
print(max(tree[1][0], tree[1][1]))