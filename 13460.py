'''
구슬 탈출
빨간 구슬, 파란구슬 각 1개
세로 : N, 가로 : M
빨간 구슬을 꺼내는게 목표. 파란 구슬을 꺼내면 안된다.
동서남북으로 기울이기가 가능하다.
빨간 구슬과 파랑 구슬이 동시에 빠져도 실패
빨간 구슬을 몇 번 기울이면 꺼낼 수 있는가?
'''

'''
현재 실패 version
'''

from collections import deque
queue=deque()
queue2=deque()
dx=[[1,0],[-1,0],[0,1],[0,-1]]

def bfs(row, col, bluerow, bluecol):
    global num
    visit[row][col]=num

    queue.append([row, col])
    queue2.append([bluerow,bluecol])
    while queue:
        leng=len(queue)
        for i in range(leng):
            data=queue.popleft()
            data2=queue2.popleft()
            for i in dx:
                t = [i[0], i[1]]
                tt=[i[0], i[1]]
                if visit[data[0]+t[0]][data[1]+t[1]]==0 and (k[data[0]+t[0]][data[1]+t[1]]=='O' or k[data[0]+t[0]][data[1]+t[1]]=='.'):
                    while visit[data[0] + t[0]][data[1] + t[1]] == 0 and (
                                k[data[0] + t[0]][data[1] + t[1]] == 'O' or k[data[0] + t[0]][data[1] + t[1]] == '.'):
                        visit[data[0] + t[0]][data[1] + t[1]]=num
                        t[0]+=i[0]
                        t[1]+=i[1]
                    k[data[0]][data[1]]='.'
                    k[data[0]+t[0]-i[0]][data[1]+t[1]-i[1]]='R'
                    queue.append([data[0]+t[0]-i[0],data[1]+t[1]-i[1]])
                    while k[data2[0] + tt[0]][data2[1] + tt[1]] == 'O' or k[data2[0] + tt[0]][data2[1] + tt[1]] == '.':
                        if k[data2[0] + tt[0]][data2[1] + tt[1]] == 'O':
                            #print("오잉")
                            return -1
                        #print(data2[0] + tt[0], data2[1] + tt[1])
                        tt[0] += i[0]
                        tt[1] += i[1]
                    k[data2[0]][data2[1]] = '.'
                    k[data2[0] + tt[0] - i[0]][data2[1] + tt[1] - i[1]] = 'B'
                    queue2.append([data2[0]+tt[0]-i[0],data2[1]+tt[1]-i[1]])

                if visit[goal[0]][goal[1]]!=0:
                    #print("con")
                    return num
                elif num>10:
                    return -1

        num += 1




N,M=map(int,input().split())
k=[[0 for i in range(M)] for i in range(N)]
visit=[[0 for i in range(M)] for i in range(N)]
goal=[]
red=[]
blue=[]
num=1
result=0
for i in range(N):
    t=input()
    for j in range(M):
        k[i][j]=t[j]
        if t[j]=='O':
            goal=[i,j]
        elif t[j]=="R":
            red=[i,j]
        elif t[j]=="B":
            blue=[i,j]
result=bfs(red[0], red[1], blue[0], blue[1])
#print(visit)
print(result)

