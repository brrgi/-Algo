import sys
from collections import deque

input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int, input().split()))

D = [0 for _ in range(N)]
Lists = deque()
for i in range(N):
    while Lists and Lists[-1][1] > A[i]:
        Lists.pop()
    while Lists and i - Lists[0][0] >= L:
        Lists.popleft()

    Lists.append((i, A[i]))
    D[i] = Lists[0][1]

print(*D)

#출 처 : https://wooooooak.github.io/algorithm/2018/12/03/%EB%B0%B1%EC%A4%8011003%EB%B2%88%EB%AC%B8%EC%A0%9C/
