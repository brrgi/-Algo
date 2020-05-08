def solution(board, moves):
    stack = []
    num=0
    leng1 = len(board)
    leng = len(moves)
    for i in (moves):
        for j in range(leng1):

            if board[j][i-1]==0:
                continue
            else:
                stack.append(board[j][i-1])
                board[j][i - 1]=0
                if len(stack)>=2 and stack[-1]==stack[-2]:
                    stack.pop()
                    stack.pop()
                    num+=2
                break

    answer = num
    return answer
