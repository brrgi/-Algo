from copy import deepcopy
m=4
n=5
board=['CCBDE', 'AAADE', 'AAABF', 'CCBBF']

def confirm(maps, row, col):
    temp = maps[row][col]
    if temp==' ':
        return 0
    if maps[row + 1][col] != temp:
        return 0
    elif maps[row][col + 1] != temp:
        return 0
    elif maps[row + 1][col + 1] != temp:
        return 0
    return [[row, col], [row + 1, col], [row, col + 1], [row + 1, col + 1]]


def down(maps, n, m):
    newMap=[[' ' for i in range(n)] for i in range(m)]
    all=[]
    for i in range(n):
        a=''
        for j in range(m):
            if maps[j][i]!=' ':
                a+=maps[j][i]
        all.append(a)
    for i in range(n):
        tt=len(all[i])-1
        t=m-1
        if all[i]!=[]:
            for j in all[i]:
                newMap[t][i]=all[i][tt]
                t-=1
                tt-=1
    return newMap

def solution(m, n, board):
    answer = 0
    board=list(map(list, board))

    while 1:
        temp=[]
        for i in range(m-1):
            for j in range(n-1):
                t=confirm(board, i,j)
                if t==0:
                    continue
                else:
                    for q in t:
                        if q not in temp:
                            temp.append(q)
        for i in temp:
            board[i[0]][i[1]]=' '
        answer+=len(temp)
        if len(temp)==0:
            break
        board=down(board, n,m)

        print(answer)
    return answer
solution(m,n,board)
