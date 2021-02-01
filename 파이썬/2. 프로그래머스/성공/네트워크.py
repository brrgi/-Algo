import sys
sys.setrecursionlimit(10**8)

def dfs(first, visit, computers, chichi):
    visit[first]=chichi
    for i in range(len(computers[first])):
        if computers[first][i]==1 and visit[i]==0:
            dfs(i, visit, computers, chichi)

def solution(n, computers):
    visit=[0 for i in range(len(computers))]
    chichi=1
    for i in range(len(computers)):
        if visit[i]==0:
            dfs(i, visit, computers, chichi)
            chichi+=1
    answer = chichi-1
    return answer
