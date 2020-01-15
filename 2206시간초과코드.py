from collections import deque
N,M=map(int, input().split())
k=[[1 for i in range(M)] for i in range(N)]     #1이 이동할 수 없는 벽
visit=[[0 for i in range(M)] for i in range(N)]
wall=deque()
dx=[[1,0],[-1,0],[0,1],[0,-1]]

queue=deque()
date=1
minnum=100000000
def bfs():
    global date
    visit[0][0]=1
    queue.append([0,0])
    while queue:
        #print(queue)
        leng=len(queue)
        date += 1

        for i in range(leng):
            data=queue.popleft()
            for j in dx:
                if data[0]+j[0]>=0 and data[0]+j[0]<N and data[1]+j[1]>=0 and data[1]+j[1]<M:
                    if visit[data[0]+j[0]][data[1]+j[1]]==0 and k[data[0]+j[0]][data[1]+j[1]]==0:
                        visit[data[0] + j[0]][data[1] + j[1]]=1
                        queue.append([data[0] + j[0],data[1] + j[1]])


for i in range(N):
    t=input()
    for j in range(M):
        k[i][j]=int(t[j])
        if t[j]=='1':
            wall.append([i,j])


while wall:
    visit = [[0 for i in range(M)] for i in range(N)]
    date=0
    re=wall.pop()
    k[re[0]][re[1]] = 0
    bfs()
    if date<minnum and visit[N-1][M-1]==1:
        #print(minnum, visit, wall)
        minnum=date
    k[re[0]][re[1]] = 1

if minnum==100000000:
    print(-1)
else:
    print(minnum)
