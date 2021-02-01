from collections import deque
import copy
t=int(input())
direct=[[-1,0], [1,0],[0,1], [0,-1]]


#탈옥 성공 여부 함수
def isSuccess(visit):
    for i in range(2):
        for j in range(w):
            if visit[0][j]!=0 or visit[0][j]==-1:
                return 1

    for i in range(2):
        for j in range(h):
            if visit[j][0]!=0 or visit[0][j]==-1:
                return 1

    return 0

#bfs 테스트 별로 초기화
def bfsInit(first):
    global queue, total
    total=1
    queue=deque()
    queue.append(first)

def visitClean():
    global visit
    for i in range(1,h-1):
        for j in range(1,w-1):
            if k[i][j]=='#':
                continue
            else:
                visit[i][j]=0

def bfs():
    global queue,visit, total, k, sum

    while isSuccess(visit)!=1:
        check = deque()
        print("Tlqkf")
        while queue:
            leng = len(queue)
            print(queue)
            for i in range(leng):
                data=queue.popleft()
                for j in direct:
                    if data[0]+j[0]>=0 or data[1]+j[1]>=0 or data[0]+j[0]<h or data[1]+j[1]<w:

                        if k[data[0]+j[0]][data[1]+j[1]]=='.' or k[data[0]+j[0]][data[1]+j[1]]=='$':
                            if visit[data[0]+j[0]][data[1]+j[1]]==0:
                                visit[data[0]+j[0]][data[1]+j[1]]+=total
                                queue.append([data[0]+j[0],data[1]+j[1]])

                        elif k[data[0]+j[0]][data[1]+j[1]]=='#':
                            if data[0] + j[0] == 0 or data[1] + j[1] == 0 or data[0] + j[0] == h - 1 or data[1] + j[1] == w - 1:
                                visit[data[0] + j[0]][data[1] + j[1]] = -1
                                sum += total
                            else:
                                if visit[data[0] + j[0]][data[1] + j[1]] == 0:
                                    visit[data[0] + j[0]][data[1] + j[1]] += total
                                    check.append([data[0] + j[0], data[1] + j[1]])
                                else:
                                    queue.append([data[0] + j[0], data[1] + j[1]])

        queue=copy.deepcopy(check)
        total+=1



for i in range(t):
    total=1
    sum=0
    h, w = map(int, input().split())
    k=[['*' for i in range(w)] for i in range(h)]
    human=[]
    for i in range(h):
        p=input()
        for j in range(w):
            k[i][j]=p[j]
            if p[j]=='$':
                human.append([i,j])

    visit=[[0 for i in range(w)] for i in range(h)]

    print(k, visit)
    queue = deque()
    bfsInit(human[0])
    bfs()
    print(visit, sum)

    visitClean()
    print(visit)
    bfsInit(human[1])
    bfs()
    print(visit, sum)

# 1
# 5 9
# ****#****
# *..#.#..*
# ****.****
# *$#.#.#$*
# *********
