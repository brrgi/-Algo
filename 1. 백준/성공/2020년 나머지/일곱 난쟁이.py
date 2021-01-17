from itertools import combinations

k=[]
for i in range(9):
    k.append(int(input()))

t=list(combinations(k,7))
for i in t:
    if sum(i)==100:
        s=list(i)
        s.sort()
        for j in s:
            print(j)
        break
