t=int(input())
for i in range(t):
    n,r = map(int, input().split())
    up=1
    down=1

    for j in range(r):
        up*=n-j
    for j in range(r):
        down*=r-j

    print("#%d %d" %((i+1), (up/down)%1234567891))