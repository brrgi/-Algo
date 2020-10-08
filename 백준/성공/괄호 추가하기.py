from collections import deque
import sys
a=int(input())
b=input()

all=deque()
first='0'
if a==1:
    print(int(b[0]))
else:
    for i in range(a//2):
        if len(all)==0:
            all.append(first+'0')
            all.append('11')
        else:
            leng=len(all)
            for j in range(leng):
                temp=all.popleft()
                if temp[-1]=='0':
                    all.append(temp+'0')
                    all.append(temp[:len(temp)-1]+'11')
                else:
                    all.append(temp+'0')
    result=-sys.maxsize
    for i in all:
        first=0
        indexing=0
        toggle=0
        stack=deque()
        while indexing<len(b):
            if indexing%2==0: #숫자
                if i[first]=='0':
                    stack.append(int(b[indexing]))
                else:
                    if toggle==0:
                        stack.append(int(b[indexing]))
                        toggle=1
                    else:
                        toggle=0
                        cal=stack.pop()
                        number=stack.pop()
                        if cal=='+':
                            stack.append(number+int(b[indexing]))
                        elif cal=='*':
                            stack.append(number*int(b[indexing]))
                        else:
                            stack.append(number-int(b[indexing]))
                first += 1
                indexing += 1
            else:             #문자
                stack.append(b[indexing])
                indexing+=1
        while len(stack)!=1:
            one=int(stack.popleft())
            two=stack.popleft()
            three=int(stack.popleft())
            if two == '+':
                stack.appendleft(one + three)
            elif two == '*':
                stack.appendleft(one * three)
            else:
                stack.appendleft(one - three)
        if stack[0]>result:
            result=stack[0]
    print(result)
