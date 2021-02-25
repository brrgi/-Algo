a=int(input())
b=list(map(int, input().split()))
plus=1
minus=1

check1=1
check2=1
for i in range(1, a):
    if b[i]>=b[i-1]:
        plus+=1
    else:
        plus=1
    if check1 < plus:
        check1 = plus

    if b[i]<=b[i-1]:
        minus+=1
    else:
        minus=1
    if check2 < minus:
        check2 = minus

print(max(check1, check2))