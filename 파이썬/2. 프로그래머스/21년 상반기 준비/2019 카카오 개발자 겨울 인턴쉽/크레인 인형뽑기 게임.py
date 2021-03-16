from collections import deque
def solution(board, moves):
    answer = 0
    stack=[]
    legnth=len(board)
    newBoard=[deque() for i in range(legnth)]

    for i in range(legnth):
        for j in range(legnth):
            if board[j][i]!=0:
                newBoard[i].append(board[j][i])

    for move in moves:
        if len(newBoard[move-1])!=0:
            data=newBoard[move-1].popleft()
            if len(stack)!=0:
                if stack[-1]==data:
                    answer+=2
                    stack.pop()
                else:
                    stack.append(data)
            else:
                stack.append(data)

    return answer