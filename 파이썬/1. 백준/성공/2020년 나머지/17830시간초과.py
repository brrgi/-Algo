#생각보다 많은 시간을 잡아 먹는다. 이진수로 변환한 후 다시 문자열로 변환하는 과정의 함수들의 시간복잡도를 조사해 볼 것.

from _collections import deque
import sys

a=int(sys.stdin.readline())

for i in range(a):
    N,M=map(str,sys.stdin.readline().split())
    N=int(N)

    stop=deque()
    possibility=[]
    for j in range(len(M)):
        if M[j]=='?':
            stop.append(j)

    table1=str.maketrans('?', '1')
    table2=str.maketrans('?', '0')
    one=M.translate(table1)
    two=M.translate(table2)
    qq=0
    q=0

    for i in range(len(one)):
        if one[i]=='1':
            qq=i
            break
    for i in range(len(two)):
        if two[i]=='1':
            q=i
            break

    one = one[qq:]
    two=two[q:]
    one='0b'+one
    two='0b'+two

    first=len(bin((2**N-1)*int(one,2)))-2
    second=len(bin((2**N-1)*int(two,2)))-2
    print(first, second)
