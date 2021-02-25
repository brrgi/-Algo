import sys
testCase=int(input())

def dfs(coreIndex, line, coreCount):
    global maxCore
    global result

    toggle=0

    if core[coreIndex][0]==0 or core[coreIndex][0]==n-1 or core[coreIndex][1]==0 or core[coreIndex][1]==n-1:    #벽에 붙어있
        dfs(coreIndex+1, line, coreCount+1)
        toggle=1

    if toggle==0:
        if temp[0] != 0 and temp[0] < result and maxCore == temp[1]:
            result = temp[0]
            maxCore = temp[1]
        elif temp[0] != 0 and maxCore < temp[1]:
            result = temp[0]
            maxCore = temp[1]


dir = [(0,1),(0,-1),(1,0),(-1,0)]
result=0
maxCore=0
for i in range(testCase):
    n=int(input())

    maxCore=0
    result=sys.maxsize
    maps=[list(map(int, input().split())) for i in range(n)]
    core=[]
    visit=[]
    for j in range(n):
        for q in range(n):
            if maps[j][q]==1:
                core.append((j,q))
                visit.append(0)

    temp=dfs(0,0,0)
