a=input()
stack=[]
b=len(a)
last=[]
result=0

def empty(stack):
    if len(stack)==0:       #비어있을 때
        return 1
    else:
        return 0

def ending(stack):
    if len(stack)!=0:       #끝났는데 안 비어져있을 때
        return 1
    else:
        return 0

def find_number(stack):
    t=len(stack)
    how=0
    sum=0
    for i in range(t):
        if str(stack[t-(i+1)]).isdigit():
            sum+=stack[t-(i+1)]     #숫자들 더하기
            stack.pop()
            how+=1          #몇 개가 숫자인지
        else:
            break
    if how==0:
        return 1
    else:
        return sum

def lastsame(stack, end, now): #last, a[i]
    global last
    if end=='(' and now==')':
        result=find_number(stack)*2
        stack.pop()
        last.pop()
        stack.append(result)
    elif end=='[' and now==']':
        result=find_number(stack)*3
        stack.pop()
        last.pop()
        stack.append(result)
    else:
        stack.append(now)
        last.append(now)


for i in range(b):
    if empty(last):
        stack.append(a[i])
        last.append(a[i])
    else:
        lastsame(stack, last[-1], a[i])
    #print(stack, last)

result=find_number(stack)
if ending(stack)==1:
    print(0)
else:
    print(result)
