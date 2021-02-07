#스트라이크 : 위치랑 값이 같은 것
#볼 : 값만 같은 것
a=int(input())
allCase=[]
isOk=[]

for i in range(9):
    string=""
    for j in range(9):
        if i==j:
            continue
        for k in range(9):
            if k==i or k==j:
                continue
            string=str(i+1)+str(j+1)+str(k+1)
            allCase.append(string)
            isOk.append(0)
print()
print(allCase)
condition=0
for i in range(a):
    t=list(map(int,input().split()))
    t[0]=str(t[0])
    for j in range(len(allCase)):
        if isOk[j]==condition:
            strike=0
            ball=0
            for w in range(3):
                if allCase[j][w]==t[0][w]:
                    strike+=1
                elif allCase[j][w] in t[0]:
                    ball+=1
            if strike==t[1] and ball==t[2]:
                isOk[j]=condition+1
    print(t[0])
    print(isOk)
    condition+=1

print(isOk.count(condition))