a = int(input())
t = list(map(int, input().split()))
result=[-1 for i in range(a)]
stack = []

for i in range(a):
    if stack == []:
        stack.append((t[i], i))
    else:
        while 1:
            if stack!=[] and stack[-1][0] < t[i]:
                temp = stack.pop()
                result[temp[1]]=t[i]
            else:
                stack.append((t[i],i))
                break

for i in result:
    print(i, end=' ')