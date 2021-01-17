import sys
from math import *
input = sys.stdin.readline

# 세그먼트 트리 생성
def init(node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]
    else:
        tree[node] = max(init(node * 2, start, (start + end) // 2), init(node * 2 + 1, (start + end) // 2 + 1, end), (end-start+1)*min(numbers[start:end+1]))
        return tree[node]


# node가 담당하는 구간 [start, end]
# 최솟값을 구해야하는 구간 [left, right]
def findMax(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]

    return max(findMax(node * 2, start, (start + end) // 2, left, right), findMax(node * 2 + 1, (start + end) // 2 + 1, end, left, right))






n=int(input())
numbers=[]
treeSize=1<<(int(ceil(log2(n)))+1)
tree=[0]*treeSize


for _ in range(n):
    numbers.append(int(input().rstrip()))

init(1,0,n-1)
print(tree)