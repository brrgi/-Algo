from collections import deque
import copy
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
maps=[[0 for i in range(M)] for i in range(N)]
for i in range(N):
    t=input()
    for j in range(M):
        k=maps[i][j]=t[j]
        if t[j]=="R":
            red=[i,j]
        elif t[j]=="B":
            blue=[i,j]
dx=[[1,0],[-1,0],[0,1], [0,-1]]

def movement(now, direction):
    distance=0
    while 1:
        row=now[0]+direction[0]
        col=now[1]+direction[1]
        if maps[row][col]=='.':
            distance+=1
            now=[row,col]
        elif maps[row][col]=='O':       #구멍에 빠짐 - 거리에 없는 숫자 반환
            return -1
        elif maps[row][col]=='#':       #현재 위치랑 이동 거리 반환
            return [now ,distance]
        else:
            distance += 1
            now = [row, col]

reds=deque()
blues=deque()
reds.append(red)
blues.append(blue)

def bfs():
    result = 0
    for i in range(10):
        result+=1
        leng=len(reds)
        for j in range(leng):
            one=reds.popleft()
            two=blues.popleft()
            for direc in dx:
                temp1=movement(one, direc)
                temp2=movement(two, direc)
                if temp1==-1:                       #빨강 구멍에 빠짐
                    if temp2==-1:                   #파랑 구멍에 빠짐 - X
                        continue
                    else:                           #빨강만 구멍에 빠짐 - O
                        return result
                else:                               #빨강 구멍에 안빠짐
                    if temp2==-1:                   #파랑 구멍에 빠짐   - x
                        continue
                    else:                           #둘 다 구멍에 안 빠짐
                        if temp1[0]==temp2[0]:      #둘 다 같은 위치에 있음
                            if temp1[1]>temp2[1]:   #빨강이 더 많이 움직임
                                temp1[0]=[temp1[0][0]-direc[0], temp1[0][1]-direc[1]]
                                reds.append(temp1[0])
                                blues.append(temp2[0])
                            else:
                                temp2[0] = [temp2[0][0] - direc[0], temp2[0][1] - direc[1]]
                                reds.append(temp1[0])
                                blues.append(temp2[0])
                        else:
                            reds.append(temp1[0])
                            blues.append(temp2[0])
    return -1
value=bfs()
print(value)
