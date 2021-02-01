from collections import defaultdict
n=int(input())
energies=[]
dic=defaultdict(set)

prev=[0 for i in range(n)]
visit=[0 for i in range(n)]
for i in range(n):
    energies.append(int(input()))

for i in range(n-1):
    a,b,c=map(int,input().split())
    dic[a-1].add((b-1, c))
    dic[b-1].add((a-1, c))


visit[0]=1
def dfs(start):
    for i in dic[start]:
        if visit[i[0]]==0:
            if start==0:
                visit[i[0]] = visit[start]+i[1]-1
                dfs(i[0])
            else:
                visit[i[0]]=visit[start]+i[1]
                prev[i[0]]=start
                dfs(i[0])

def dfs2(start, nowEnergy):
    result=start
    hi=0
    for v in dic[start]:
        if v[0]==prev[start]:
            hi=v[1]
    if nowEnergy-hi>=0:
        result=dfs2(prev[start], nowEnergy-hi)
    return result

dfs(0)
# print("energies",energies)
# print("dic",dic)
# print("visit",visit)
# print("prev",prev)

for i in range(n):
    if i==0:
        print(1)
    else:
        if energies[i]>=visit[i]:
            print(1)
        else:
            print(dfs2(i, energies[i])+1)
