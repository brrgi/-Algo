from itertools import combinations
from copy import deepcopy
n,m,d=map(int, input().split())

maps=[]
comb=[i for i in range(m)]
enem=[]
for i in range(n):
    t=list(map(int,input().split()))
    for j in range(len(t)):
        if t[j]==1:
            enem.append([i,j])
    maps.append(t)

combs=list(combinations(comb, 3))
result=-1
for comb in combs:
    how=0
    enemy=deepcopy(enem)
    while enemy:
        remov=[]
        for i in comb:
            row=n
            col=i

            target=[]
            distance=33
            left=16
            for j in enemy:
                nowDist=abs(row-j[0])+abs(col-j[1])
                if d>=nowDist:
                    if nowDist<distance:
                        distance=nowDist
                        target=j
                        left=j[1]
                    elif nowDist==distance:
                        if j[1]<left:
                            target=j
                            left=j[1]
            if target not in remov:
                if target!=[]:
                    remov.append(target)

        for i in remov:
            enemy.remove(i)
            how+=1
        for i in range(len(enemy)):
            enemy[i][0]+=1
        for i in enemy[:]:
            if i[0]==n:
                enemy.remove(i)
    if result<how:
        result=how
print(result)
