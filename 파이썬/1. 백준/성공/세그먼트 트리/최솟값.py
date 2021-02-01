import sys
from math import ceil, log
input = sys.stdin.readline

# 세그먼트 트리 생성
def init(node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]
    else:
        tree[node] = min(init(node * 2, start, (start + end) // 2),init(node * 2 + 1, (start + end) // 2 + 1, end))
        return tree[node]


# node가 담당하는 구간 [start, end]
# 최솟값을 구해야하는 구간 [left, right]
def findMin(node, start, end, left, right):
    if left > end or right < start:
        return 1000000000

    if left <= start and end <= right:
        return tree[node]

    return min(findMin(node * 2, start, (start + end) // 2, left, right), findMin(node * 2 + 1, (start + end) // 2 + 1, end, left, right))






n,m=map(int,input().split())
numbers=[]
treeSize=(2**ceil(log(n,2)))*2
tree=[1000000000]*treeSize


for _ in range(n):
    numbers.append(int(input().rstrip()))

init(1,0,n-1)
for i in range(m):
    a,b=map(int, input().split())
    print(findMin(1,0,n-1,a-1,b-1))