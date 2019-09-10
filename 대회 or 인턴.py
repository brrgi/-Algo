a,b,c=map(int,input().split())      #여학생, 남학생, 인턴쉽 인원

k=a//2  #몫
kk=a%2  #나누기


if k>b:
    max=b
else:
    max=k

count1=(a-max*2)+(b-max)
if count1<c:
    c=c-count1
    cc=c%3
    ccc=c//3
    if cc==0:
        print(max-ccc)
    else:
        print(max-ccc-1)
else:
    print(max)
