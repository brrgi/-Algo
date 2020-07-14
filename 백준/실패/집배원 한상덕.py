from collections import deque

n=int(input())
house=[list(map(str,input())) for i in range(n)]
height=[list(map(int,input().split())) for i in range(n)]
visit=[[0 for i in range(n)] for i in range(n)]
dx=[(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,0),(-1,-1),(-1,1)]
p=[]
houseBoundary=[]
boundary=[]
houseVisit=0

for i in range(n):
    for j in range(n):
        if house[i][j]!='.' and height[i][j] not in houseBoundary:
            houseBoundary.append(height[i][j])
        if house[i][j]=='P':
            p=[i,j]
            houseVisit+=1
        elif house[i][j]=='K':
            houseVisit+=1

for i in height:
    for j in i:
        if j not in boundary:
            boundary.append(j)

houseBoundary.sort()
boundary.sort()
houseStart, houseEnd=houseBoundary[0], houseBoundary[-1]
boundaryStart, boundaryEnd=boundary[0], boundary[-1]

queue=deque()

#입력 : 움직일 수 있는 범위 값
#출력 : 모든 집을 방문했는지
def bfs(start, end):
    global visit
    queue = deque()

    queue.append(p)
    visit[p[0]][p[1]] = 1
    visit = [[0 for i in range(n)] for i in range(n)]
    houseVisit=0
    while queue:
        leng=len(queue)
        for i in range(leng):
            data = queue.popleft()
            for j in dx:
                if 0<=data[0]+j[0]<n and 0<=data[1]+j[1]<n:
                    if start<=height[data[0]+j[0]][data[1]+j[1]]<=end and visit[data[0]+j[0]][data[1]+j[1]]==0:
                        if house[data[0]+j[0]][data[1]+j[1]]!='.':
                            houseVisit+=1
                        visit[data[0] + j[0]][data[1] + j[1]]=1
                        queue.append([data[0] + j[0],data[1] + j[1]])
    print(visit)
    return houseVisit

start, end = boundary.index(houseEnd), len(boundary)-1
print("ggg",houseBoundary)
print("ee",boundary)
print(boundaryStart, boundary[end])
while end>=0:
    result=bfs(boundaryStart, boundary[end])
    if houseVisit==result:
        end-=1
    else:
        break
end=end+1
print(boundary[end],end)
Right=boundary[end]

print("==========절취선==========")

start=0

while start<=end:
    result = bfs(boundary[start], Right)
    print("sdfdfdsfasd",result,boundary[start], Right)
    if houseVisit == result:
        start+=1
    else:
        break
print(start)
start-=1
Left=boundary[start]

print(Right,Left)
print(Right-Left)

