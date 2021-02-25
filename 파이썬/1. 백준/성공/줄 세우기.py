a=int(input())
hi = list(map(int, input().split()))
result=[]
for i in range(a):
    result.insert((i-hi[i]),i+1)

for i in range(a):
    print(result[i], end=" ")