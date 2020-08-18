from copy import deepcopy
from collections import deque
import sys


def all(first, second, third, maps, n, m):
    result = sys.maxsize
    for i in range(n):
        for j in range(m):
            if maps[i][j] == '.':
                if result > first[i][j] + second[i][j] + third[i][j]:
                    result = first[i][j] + second[i][j] + third[i][j]
            elif maps[i][j] == '#':
                if result > first[i][j] + second[i][j] + third[i][j] - 2:
                    result = first[i][j] + second[i][j] + third[i][j] - 2
    return result


def bfs(one, maps):
    visit = [[-1 for i in range(m + 2)] for i in range(n + 2)]
    queue = deque()
    queue.append(list(one))
    number = 0
    visit[one[0]][one[1]] = 0
    i = 0
    open = deque()
    while queue:
        data = queue.popleft()
        for j in go:
            dx = data[0] + j[0]
            dy = data[1] + j[1]
            if dx < 0 or dx > n + 1 or dy < 0 or dy > m + 1:
                continue
            if visit[dx][dy] == -1:
                if maps[dx][dy] == '.' or maps[dx][dy] == '$':
                    visit[dx][dy] = number
                    queue.append([dx, dy])
                elif maps[dx][dy] == '#':
                    open.append([dx, dy])
                    visit[dx][dy] = number + 1
        if len(queue) == 0:
            queue = deepcopy(open)
            open = deque()
            number += 1
    return visit


test = int(input())
go = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for _ in range(test):
    n, m = map(int, input().split())
    maps = []
    man = []
    maps.append(['.' for i in range(m + 2)])
    for i in range(n):
        t = list('.' + input() + '.')
        for j in range(1, m + 1):
            if t[j] == '$':
                man.append((i + 1, j))
        maps.append(t)
    maps.append(['.' for i in range(m + 2)])
    first = bfs(man[0], maps)
    second = bfs(man[1], maps)
    third = bfs((0, 0), maps)
    ans = all(first, second, third, maps, n, m)

    print(ans)
