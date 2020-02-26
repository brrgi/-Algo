from collections import deque
n,m=map(int,input().split())
go=[[] for i in range(n)]
indegree=[0 for i in range(n)]
for i in range(m):
    a,b=map(int, input().split())
    a=a-1
    b=b-1
    go[a].append(b)
    indegree[b]+=1
queue=deque()
for i in range(n):
    if indegree[i]==0:
        queue.append(i)

while queue:
    #print(queue, indegree)
    data=queue.popleft()

    leng=len(go[data])
    print(data + 1, end=' ')

    for i in range(leng):

        indegree[go[data][i]]-=1
        if indegree[go[data][i]]==0:
            queue.append(go[data][i])
