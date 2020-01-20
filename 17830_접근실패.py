from _collections import deque
a=int(input())

for i in range(a):
    N,M=map(str,input().split())
    N=int(N)
    print(N,M)
    possibility=deque()
    possibility.append(M)
    stop=deque()

    for j in range(len(M)):
        if M[j]=='?':
            stop.append(j)

    while stop:
        leng=len(possibility)
        location = stop.popleft()
        for i in range(leng):
            data=possibility.popleft()
            possibility.append(data[:location] + '1' + data[location + 1:])
            possibility.append(data[:location] + '0' + data[location + 1:])

    #print(possibility)

