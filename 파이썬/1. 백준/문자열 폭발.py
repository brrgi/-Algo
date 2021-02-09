a=input()
b=input()

bAsci=[]

stack=[]
asci=[]

for i in range(10):
    asci.append(48+i)
for i in range(26):
    asci.append(i+65)
    asci.append(i+97)
asci.sort()
for i in b:
    bAsci.append(asci.index(ord(i)))

last=bAsci[-1]

if len(b)>len(a):
    print(a)
    exit()
for i in a:
    if asci.index(ord(i))==last:
        check=0
        if len(stack)>=len(bAsci)-1:
            for j in range(len(bAsci)-1):
                if bAsci[len(bAsci)-(2+j)]==asci.index(ord(stack[len(stack)-(1+j)])):
                    check+=1
                else:
                    check=0
                    stack.append(i)
                    break
            if check==len(bAsci)-1:
                for j in range(len(bAsci) - 1):
                    stack.pop()

        else:
            stack.append(i)
    else:
        stack.append(i)

if stack==[]:
    print("FRULA")
else:
    print("".join(stack))