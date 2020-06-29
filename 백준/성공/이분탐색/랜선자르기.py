k,n=map(int,input().split())
t=[int(input()) for i in range(k)]

start=0
end=max(t)
total=0
all=[]
answer=0

while start<=end:
    if start+end==1:
        mid=1
    else:
        mid=(start+end)//2

    all=[]
    for i in range(k):
        all.append(t[i]//mid)

    if sum(all)>=n:
        answer=mid
        start=mid+1
    else:
        end=mid-1
print(answer)
