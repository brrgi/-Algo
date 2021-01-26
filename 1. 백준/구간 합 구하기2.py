import sys
from math import ceil, log
input = sys.stdin.readline

# 세그먼트 트리 생성
def init(node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node]
    else:
        tree[node] = init(node * 2, start, (start + end) // 2) + init(node * 2 + 1, (start + end) // 2 + 1, end)
        return tree[node]


# 구간 합 구하기
# node가 담당하는 구간 [start, end]
# 합을 구해야하는 구간 [left, right]
def treeSum(node, start, end, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[node]

    return treeSum(node * 2, start, (start + end) // 2, left, right) + treeSum(node * 2 + 1, (start + end) // 2 + 1, end, left, right)


def update(node, start, end, index, diff):
    if index < start or index > end:
        return

    tree[node] += diff

    if start != end:
        update(node * 2, start, (start + end) // 2, index, diff)
        update(node * 2 + 1, (start + end) // 2 + 1, end, index, diff)






n,m,k=map(int,input().split())
numbers=[]
treeSize=(2**ceil(log(n,2)))*2
tree=[0]*treeSize


for _ in range(n):
    numbers.append(int(input().rstrip()))

init(1,0,n-1)
for i in range(m+k):
    temp=list(map(int, input().split()))
    a=temp[0]
    b=temp[1]
    c=temp[2]
    if temp[0]==1:
        for j in range(b,c+1):
            update(1, 0, n-1, j-1, temp[3])
    else:
        print(treeSum(1, 0, n - 1, b - 1, c - 1))   #(node, start, end, left, right)
