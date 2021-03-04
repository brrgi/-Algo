import sys
from collections import deque

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 오른쪽, 아래, 왼쪽, 위


def solution(board):
    answer = 0
    n=len(board)
    visit = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    startRight = [0, 1, 0, 100]  # row, col, direction(가로) ,currentValue
    startDown = [1, 0, 1, 100]
    queue = deque()
    if board[0][1]==0:
        visit[0][1] = 100
        queue.append(startRight)
    if board[1][0]==0:
        visit[1][0] = 100
        queue.append(startDown)

    # print(queue)
    def bfs():
        while queue:
            data = queue.popleft()

            for i in range(4):
                newRow = data[0] + dir[i][0]
                newCol = data[1] + dir[i][1]
                if 0 <= newRow < n and 0 <= newCol < n and board[newRow][newCol] == 0:
                    if i == 1 or i == 3:  # 세로
                        if data[2] == 0:  # 가로
                            nextVal = data[3] + 600
                        else:  # 세로
                            nextVal = data[3] + 100
                        nextDir = 1
                        if visit[newRow][newCol] >= nextVal:
                            visit[newRow][newCol] = nextVal
                            # print("1", data, "->", [newRow, newCol, nextDir, nextVal])
                            queue.append([newRow, newCol, nextDir, nextVal])
                    else:  # 가로
                        if data[2] == 0:  # 가로
                            nextVal = data[3] + 100
                        else:  # 세로
                            nextVal = data[3] + 600
                        nextDir = 0
                        if visit[newRow][newCol] >= nextVal:
                            visit[newRow][newCol] = nextVal
                            # print("2", data, "->", [newRow, newCol, nextDir, nextVal])
                            queue.append([newRow, newCol, nextDir, nextVal])

    bfs()
    # for i in visit:
    #     print(i)
    answer=visit[n-1][n-1]
    return answer


board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
solution(board)
