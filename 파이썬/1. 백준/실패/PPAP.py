import sys
import copy
input=sys.stdin.readline
t=input()

while 1:
    c=copy.deepcopy(t)
    length = len(t)
    for i in range(length - 3):
        if t[i:i + 4] == 'PPAP':
            t = t[:i] + "P" + t[i + 4:]
            break
    if c==t:
        break


if t=='P':
    print('PPAP')
else:
    print("NP")
    
# 11번째 줄을 바꾸어야함 저런식으로 하면 시간 복잡도 O(n)이 추가되므로 스택으로 바꿀 
