a=int(input())
queue=[]
dx=[[1,0],[-1,0],[0,1],[0,-1]]
def bfs(row ,col, k):
    queue.append([row,col])
    visit[row][col]=1

    leng=len(queue)
    while len(queue)!=0 and visit[n][m]==0:

        leng = len(queue)
        for i in range(leng):
            data=queue.pop(0)

            for j in dx:
                if visit[data[0] + j[0]][data[1] + j[1]] == 0 and k[data[0] + j[0]][data[1] + j[1]]:
                    visit[data[0] + j[0]][data[1] + j[1]] = 1
                    queue.append([data[0] + j[0], data[1] + j[1]])


for i in range(a):
    m,n,k=map(int, input().split())     #가로 , 세로, 위치의 개수
    t = [[0 for i in range(m + 2)] for j in range(n + 2)]
    visit = [[0 for i in range(m + 2)] for j in range(n + 2)]
    number=0
    queue = []
    for i in range(n + 2):              #배열의 바깥부분들 표시
        for j in range(m + 2):
            if i == 0 or i == n + 1 or j == 0 or j == m + 1:
                visit[i][j] = 1

    for j in range(k):                  #2차원 배열 완성
        tt=input().split()
        t[int(tt[1])+1][int(tt[0])+1]=1

    for i in range(1,n+1):
        for j in range(1,m+1):
            if t[i][j]==1 and visit[i][j]==0:
                bfs(i,j, t)
                number+=1

    print(number)
