a,b=map(int, input().split())
k=[input() for i in range(a)]
kk=[input() for i in range(b)]
k=set(k)
kk=set(kk)
kkk=k.intersection(kk)
kkk=list(kkk)
kkk.sort()
print(len(kkk))
for i in kkk:
    print(i)
