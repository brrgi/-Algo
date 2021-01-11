n,m=map(int,input().split())

k=[list(map(int,input().split())) for i in range(n)]

for i in range(1,m):
    k[0][i]=k[0][i-1]+k[0][i]

for i in range(1,n):
    k[i][0]=k[i][0]+k[i-1][0]

for i in range(1,n):
    for j in range(1,m):
        k[i][j]=max(k[i-1][j], k[i-1][j-1], k[i][j-1])+k[i][j]

print(k[n-1][m-1])
