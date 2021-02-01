#pypy3로는 시간초과가 해결된다.

N=int(input())
k=[]
for i in range(N):
    k.append(int(input())-1)
k.sort()
sum=0
for i in range(len(k)):
    sum+=abs(k[i]-i)
print(sum)

