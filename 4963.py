import sys
sys.setrecursionlimit(10**6)
dx=[[1,0], [-1,0], [0,1], [0,-1],[1,1], [-1,1], [1,-1], [-1,-1]]
def dfs(row, col):
    for j in dx:
        if row+j[0]>=0 and row+j[0]<h and col+j[1]>=0 and col+j[1]<w:
            if k[row+j[0]][col+j[1]]==1 and visit[row+j[0]][col+j[1]]==0:
                visit[row+j[0]][col+j[1]]=1
                dfs(row+j[0], col+j[1])

while 1:
    w, h=map(int, input().split())
    if w+h==0:
        break
    k=[]
    number=0
    visit=[[0 for i in range(w)] for j in range(h)]
    for i in range(h):
        k.append(list(map(int,input().split())))
	
    for i in range(h):
        for j in range(w):
            if visit[i][j]==0 and k[i][j]==1:
            	visit[i][j]=1
            	dfs(i,j)
            	number+=1

    print(number)
