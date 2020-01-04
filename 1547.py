a=int(input())
k=[0,1,2,3]
cup=1
for i in range(a):
    b,c=map(int,input().split())
    if cup==b:
        cup=c
    elif cup==c:
        cup=b
    else:
        k[b]=c
        k[c]=b
print(cup)
