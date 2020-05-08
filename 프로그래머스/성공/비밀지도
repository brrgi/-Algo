def trans(number1, number2, n):
    k=''
    t=bin(number1)[2:]
    tt=bin(number2)[2:]
    if len(t)!=n:
        t='0'*(n-len(t))+t
    if len(tt)!=n:
        tt='0'*(n-len(tt))+tt
    t=list(t)
    tt=list(tt)
    print(t, tt)
    for i in range(n):
        if t[i]=='1' or tt[i]=='1':
            k=k+'#'
        else:
            k=k+' '
    return k
def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(trans(arr1[i], arr2[i], n))
    print(answer)
    return answer
