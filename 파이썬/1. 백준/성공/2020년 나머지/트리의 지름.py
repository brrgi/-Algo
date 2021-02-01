from collections import deque
a=int(input())

k=[[] for i in range(a+1)]
visit=[0 for i in range(a+1)]

for i in range(a-1):
    t=list(map(int,input().split()))
    k[t[0]].append([t[1],t[2]])
    k[t[1]].append([t[0],t[2]])


queue=deque()
def bfs(start):
    queue.append(start)
    while queue:
        leng=len(queue)
        for i in range(leng):
            data=queue.popleft()
            if k[data]!=[]:
                for j in k[data]:
                    if visit[j[0]]==0:
                        queue.append(j[0])
                        visit[j[0]]=j[1]+visit[data]

bfs(1)
firstmax=visit.index(max(visit))
visit=[0 for i in range(a+1)]
bfs(firstmax)
print(max(visit))
