import sys
def hwakIn():
    toggle=0
    for i in range(5):
        if sum(visit[i])==5:
            toggle+=1

    for i in range(5):
        hiLeeRe=0
        for j in range(5):
            if visit[j][i]==1:
                hiLeeRe+=1
        if hiLeeRe==5:
            toggle+=1
    hiLeeRe = 0
    byeLeeRe = 0
    for i in range(5):
        if visit[i][i]==1:
            hiLeeRe+=1
        if visit[4-i][i]==1:
            byeLeeRe+=1
    if hiLeeRe==5:
        toggle+=1
    if byeLeeRe==5:
        toggle+=1
    return toggle


a=[list(map(int,input().split())) for _ in range(5)]
dic = dict()
b=[list(map(int,input().split())) for _ in range(5)]
visit=[[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        dic[a[i][j]]=(i,j)

start=1
t=0
for i in range(5):
    for j in range(5):
        visit[dic[b[i][j]][0]][dic[b[i][j]][1]]=1
        if hwakIn()>=3:
            print(start)
            t=1
            break;
        start+=1
    if t==1:
        break;