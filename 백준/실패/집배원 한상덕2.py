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
            for i in dx:
                if 0<=data[0]+i[0]<n and 0<=data[1]+i[1]<n:
                    if start<=height[data[0]+i[0]][data[1]+i[1]]<=end and visit[data[0]+i[0]][data[1]+i[1]]==0:
                        if house[data[0]+i[0]][data[1]+i[1]]!='.':
                            houseVisit+=1
                        visit[data[0] + i[0]][data[1] + i[1]]=1
                        queue.append([data[0] + i[0],data[1] + i[1]])

    return houseVisit

start, end = boundary.index(houseEnd), len(boundary)-1


while start<=end:
    mid=(start+end)//2
    result=bfs(boundaryStart, boundary[mid])
    if houseVisit==result:
        end=mid-1
    else:
        start=mid+1
 


Right=boundary[mid]

# print("==========절취선==========")

start=0
end=boundary.index(houseStart)

while start<=end:
    mid=(start+end)//2
    if houseVisit==bfs(boundary[mid], Right):
        end=mid-1
    else:
        start=mid+1
 


Left=boundary[mid]

print(Right-Left)

