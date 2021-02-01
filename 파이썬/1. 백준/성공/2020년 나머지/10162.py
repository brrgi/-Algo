# A, B, C에 지정된 시간 5분 1분 10초
a=int(input())
A=300
B=60
C=10

num=[0,0,0]

if a//A!=0:
    num[0] = a // A
    a=a-(A*(a//A))



if a//B!=0:
    num[1] = a // B
    a=a-(B*(a//B))



if a//C!=0:
    num[2] = a // C
    a=a-(C*(a//C))

if a==0:
    print(num[0], num[1], num[2])
else:
    print(-1)
