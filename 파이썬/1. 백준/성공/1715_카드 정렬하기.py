import heapq
import sys
sys.stdin.readline

n=int(input())
heap=[]
for i in range(n):
    heapq.heappush(heap, int(input()))

result=0
for i in range(n-1):
    a=heapq.heappop(heap)
    b=heapq.heappop(heap)
    result+=a+b
    heapq.heappush(heap,a+b)

print(result)