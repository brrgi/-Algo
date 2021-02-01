a=int(input())
k=[[0 for i in range(a)] for i in range(a)]

newk=[0 for i in range(a//2) for i in range(a//2)]
v=0
def new(kk, line):
    global v
    newk = [[0 for i in range(line // 2)] for i in range(line // 2)]
    #print(kk, line)
    if line==1 and len(kk)!=0:
        print(kk[0][0])
        return 1
    else:
        for i in range(line//2):
            for j in range(line//2):
                c=[0 ,0 ,0 ,0]
                c[0]=kk[i*2][j*2]
                c[1]=kk[(i*2)+1][j*2]
                c[2]=kk[i*2][(j*2)+1]
                c[3]=kk[(i*2)+1][(j*2)+1]
                c.sort()
                newk[i][j]=c[-2]
        new(newk, line//2)



for i in range(a):
    t=input().split()
    for j in range(a):
        k[i][j]=int(t[j])


new(k, a)
