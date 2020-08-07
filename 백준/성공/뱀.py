from collections import deque
dx=[[0,1], [1,0], [0,-1], [-1,0]]   #오른쪽, 아래, 위, 아래
now=0

n=int(input())
board=[[0 for i in range(n)] for i in range(n)]
earthworm=[[0,0]]
k=int(input())
kList=[list(map(int,input().split())) for i in range(k)]
l=int(input())
second=deque()
direction=deque()

for i in range(l):
    e=input().split()
    second.append(int(e[0]))
    direction.append(e[1])

for i in range(k):
    board[kList[i][0]-1][kList[i][1]-1]=1

result=0
earthworm=deque()
earthworm.append([0,0])

while 1:
    x=earthworm[-1][1]+dx[now][1]
    y=earthworm[-1][0]+dx[now][0]
    # print("현재", y, x)
    #Step1 벽인지 확인
    if x<0 or x>=n or y<0 or y>=n or ([y,x] in earthworm):
        break

    #Step2 사과 있는지 확인 후 조치
    if board[y][x]==1:
        board[y][x]=0
        earthworm.append([y,x])
    else:
        earthworm.append([y,x])
        earthworm.popleft()
    result+=1
    
    #Step3 방향 전환
    if result in second:
        second.popleft()
        value=direction.popleft()
        if value=='D':
            now=(now+1)%4
        else:
            now=now-1
            if now==-1:
                now=3

print(result+1)
