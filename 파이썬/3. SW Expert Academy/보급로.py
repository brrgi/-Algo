# import sys
# sys.setrecursionlimit(10**8)
from collections import deque
t=int(input())
notVisit=100000000
dx=[(1,0),(-1,0),(0,1),(0,-1)]


for i in range(t):
    n=int(input())
    maps=[list(map(int,input())) for i in range(n)]
    visit=[[notVisit for _ in range(n)] for _ in range(n)]
    visit[0][0]=maps[0][0]

    queue=deque()
    queue.append((0,0))

    def bfs():
        while queue:
            data= queue.popleft()
            if data[0] == n - 1 and data[1] == n - 1:
                continue
            for i in dx:
                newRow = data[0] + i[0]
                newCol = data[1] + i[1]
                if 0 <= newRow < n and 0 <= newCol < n:
                    if visit[data[0]][data[1]] + maps[newRow][newCol] < visit[newRow][newCol]:
                        visit[newRow][newCol] = visit[data[0]][data[1]] + maps[newRow][newCol]
                        queue.append((newRow,newCol))


    bfs()
    print("#%d %d" % (i + 1, visit[n - 1][n - 1]))

    """
    -import sys 함수 사용 불가능 하기 때문에 안되는 방식
    
    def dfs(row, col):
        if row == n - 1 and col == n - 1:
            return
        for i in dx:
            newRow=row+i[0]
            newCol=col+i[1]
            if 0<=newRow<n and 0<=newCol<n:
                if visit[row][col]+maps[newRow][newCol]<visit[newRow][newCol]:
                    visit[newRow][newCol]=visit[row][col]+maps[newRow][newCol]
                    dfs(newRow, newCol)

    dfs(0,0)
    """


