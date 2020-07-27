import sys
input=sys.stdin.readline
a=int(input())
k=[]
kk=[]
now=[]

for i in range(a):
    t=list(map(int,input().split()))
    if t[0]<3 or (t[0]==3 and t[1]==1): #3월 1일 이전꺼
        k.append([t[2], t[3]])
    else:
        now = k[-1]
        if t[0]<now[0] or (t[0]==now[0] and t[1]<now[1]):  # 3월 1일 이전꺼랑 연결 가능
            kk.append([t[2], t[3]])
        break
number=0
for i in range(len(k),a):
    if kk==[]:
        break
    else:
        if t[0]>=12:
            break
        elif t[0]<now[0] or (t[0]==now[0] and t[1]<now[1]):  # 시작 점 3월 1일 이전꺼
            kk.append([t[2], t[3]])
            if now !=kk[-1]:
                now = kk[-1]
                number+=1
        else:
            now=kk[-1]
            kk=[]
    t = list(map(int, input().split()))
print(number)
