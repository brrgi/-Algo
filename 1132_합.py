visit=[0 for i in range(10)]

n=int(input())
dic=dict()
for i in range(10):
    dic[chr(65+i)]=0

# print(dic)
alp=[]
for i in range(n):
    t=input()
    alp.append(t)
    t=t[::-1]
    for j in range(len(t)):
        visit[ord(t[j])-65]+=1*(10**j)
    # print(visit)
print(visit)
start=9
while visit.count(0)!=10:
    k=visit.index(max(visit))
    dic[chr(65+k)]=start
    start-=1
    visit[k]=0

for i in range(n):
    for j in range(10):
        alp[i]=alp[i].replace(chr(65+j), str(dic[chr(65+j)]))

alp=list(map(int, alp))
print(sum(alp))