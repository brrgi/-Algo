a,b=map(int, input().split())
k=[]
for i in range(a-1):
    if b-(a-(i+1))>0 and b!=a-i:

        if b-(a-i-1)>=26:
            k.append(26)
            b=b-26
            continue
        else:
            k.append(b-a+i+1)
            b=a-i-1
            continue
    if b==0:
        b=-1
        break
    k.append(1)
    b=b-1
if 0<b<=26:
    k.append(b)
    b=0
if len(k)!=a or b!=0:
    print("!")
else:
    k.sort()
    for i in range(len(k)):
        print(chr(64+k[i]), end='')



