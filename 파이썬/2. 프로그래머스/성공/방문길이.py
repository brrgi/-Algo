dirs="LULLLLLLU"

def solution(dirs):
    answer = 0
    dx=[(-1,0),(1,0),(0,1),(0,-1)]
    gil=[]
    now=[0,0]
    for i in dirs:
        if i=='U':
            row=dx[0][0]+now[0]
            col=dx[0][1]+now[1]
            if -5 <= row <= 5 and -5 <= col <= 5:
                if [now[0], now[1], row, col] not in gil:
                    gil.append([now[0], now[1], row, col])
                now=[row, col]
        elif i=='D':
            row=dx[1][0]+now[0]
            col=dx[1][1]+now[1]
            if -5 <= row <= 5 and -5 <= col <= 5:
                if [row, col ,now[0], now[1]] not in gil:
                    gil.append([row, col ,now[0], now[1]])
                now = [row, col]
        elif i=='R':
            row=dx[2][0]+now[0]
            col=dx[2][1]+now[1]
            if -5 <= row <= 5 and -5 <= col <= 5:
                if [now[0], now[1], row, col] not in gil:
                    gil.append([now[0], now[1], row, col])
                now = [row, col]
        else:
            row=dx[3][0]+now[0]
            col=dx[3][1]+now[1]
            if -5 <= row <= 5 and -5 <= col <= 5:
                if [row, col ,now[0], now[1]] not in gil:
                    gil.append([row, col ,now[0], now[1]])
                now = [row, col]



    answer=len(gil)
    return answer

print(solution(dirs))
