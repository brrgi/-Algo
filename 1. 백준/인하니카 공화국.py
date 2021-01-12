import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)
start=0
results=0

def dfs(start):
    if start==0:
        visit[0]=1
        for i in range(n):
            if visit[i]==0 and maps[start][i]!=0:
                visit[i]=1
                up[i]=maps[start][i]
                dfs(i)
    else:
        visit[start]=1
        for i in range(n):
            if visit[i]==0 and maps[start][i]!=0:
                visit[i]=1
                up[i]=maps[start][i]
                dfs(i)


def recur(start):
    result=0
    global results
    if start==0:    #1인 경우
        for i in range(n):
            if visit[i]==0 and maps[start][i]!=0:
                visit[i]=1
                temp=recur(i)
                results+=temp
        return results
    else:
        for i in range(n):
            if visit[i]==0 and maps[start][i]!=0:
                visit[i]=1
                result+=recur(i)
        if result==0:
            return up[start]
        else:
            if result<up[start]:
                up[start]=result
            return up[start]

    return result

testcase=int(input())
for _ in range(testcase):
    n,m=map(int,input().split())
    up=[-1 for _ in range(n)]       #위의 부모를 확인할 것
    visit=[0 for _ in range(n)]
    maps=[[0 for _ in range(n)] for _ in range(n)]

    for i in range(m):
        a,b,cost=map(int,input().split())
        maps[a-1][b-1]=cost
        maps[b-1][a-1]=cost
    dfs(start)
    visit = [0 for _ in range(n)]

    print(recur(start))
