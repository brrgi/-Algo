n,m=map(int, input().split())
k=[]
kk=[]
check=[0 for i in range(n)]
for i in range(n):
	a=int(input())
	k.append(a)
for j in range(m):
	b=int(input())
	kk.append(b)
for i in range(len(kk)):
	for j in range(len(k)):
		if kk[i] >= k[j]:
			check[j]+=1
			break
print(check.index(max(check))+1)
