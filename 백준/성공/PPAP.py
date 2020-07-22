import sys
input=sys.stdin.readline
t=input().rstrip()

stack=[]
i=0
while i<len(t):
    if t[i]=='P':
        stack.append(t[i])
        i+=1
    else:
        if len(stack)>=2 and i<len(t)-1:
            if stack[-1]=='P' and stack[-2] =='P' and t[i+1]=='P':
                stack.pop()
                i+=2
            else:
                stack.append(t[i])
                break
        else:
            stack.append(t[i])
            break

if ''.join(stack)=="P":
    print("PPAP")
else:
    print("NP")
