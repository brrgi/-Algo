a=int(input())

def cycle(k, value):       #a=list
    first=value
    ast=[]
    while 1:
        #print(k[value], first)
        ast.append(value+1)
        if k[value]==(first+1):
            return ast
        elif k[value]==(value+1):
            return -1
        else:
            value=k[value]-1


for i in range(a):
    num=int(input())
    k=list(map(int,input().split()))
    kkk=[0 for i in range(num)]
    for j in range(num):
        z=cycle(k, j)
        if z!=-1:
            for x in z:
                kkk[x-1]=1
    #print(kkk)
    print(kkk.count(0))
