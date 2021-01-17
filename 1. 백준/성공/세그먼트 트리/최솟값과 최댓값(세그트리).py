import sys
from math import *
input = sys.stdin.readline

# 세그먼트 트리 생성
def initMin(node, start, end):
    if start == end:
        minValue[node] = l[start]
        return minValue[node]
    else:
        minValue[node] = min(initMin(node * 2, start, (start + end) // 2), initMin(node * 2 + 1, (start + end) // 2 + 1, end))
        return minValue[node]

def initMax(node, start, end):
    if start == end:
        maxValue[node] = l[start]
        return maxValue[node]
    else:
        maxValue[node] = max(initMax(node * 2, start, (start + end) // 2), initMax(node * 2 + 1, (start + end) // 2 + 1, end))
        return maxValue[node]

# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def mini(node, start, end, left, right):
    if left > end or right < start:
        return sys.maxsize

    if left <= start and end <= right:
        return minValue[node]

    return min(mini(node * 2, start, (start + end) // 2, left, right), mini(node * 2 + 1, (start + end) // 2 + 1, end, left, right))

def maxi(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return maxValue[node]

    return max(maxi(node * 2, start, (start + end) // 2, left, right), maxi(node * 2 + 1, (start + end) // 2 + 1, end, left, right))



n,m=map(int, input().split())
l = []
treeSize=1<<(int(ceil(log2(n)))+1)
maxValue = [0] * treeSize
minValue = [0] * treeSize

for _ in range(n):
    l.append(int(input()))

initMin(1,0,n-1)
initMax(1,0,n-1)

for _ in range(m):
    a,b=map(int,input().split())

    print(mini(1, 0, n - 1, a - 1, b - 1), end=' ')
    print(maxi(1,0,n-1,a-1,b-1))

