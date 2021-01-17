n=int(input())
m=int(input())

start=1
end=m

while start<=end:
    mid=(start+end)//2

    a=0
    for i in range(1, n+1):
        a+=min(mid//i, n)

    if a>=m:
        result=mid
        end=mid-1
    else:
        start=mid+1
print(result)