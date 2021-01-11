import sys

n, m = map(int, sys.stdin.readline().split())

parents = [i for i in range(n + 1)]  # 먼저 모든 노드의 루트를 자신으로 지정한다.


def Find(x):  # x로 들어온 원소의 루트노드 반환
    if x == parents[x]:  # 루트와 같다면 반환
        return x
    else:  # 루트노드 찾아가기
        y = Find(parents[x])
        parents[x] = y
        return y


def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y:  # 합쳐준다.
        parents[y] = x


for _ in range(m):
    command, a, b = map(int, sys.stdin.readline().split())
    if command == 0:  # 합친다
        Union(a, b)


    elif command == 1:  # 각 루트 찾아서 비교
        a_parents = Find(a)
        b_parents = Find(b)
        if a_parents == b_parents:  # 루트가 같으면
            print("YES")
        else:
            print("NO")

print(parents)

