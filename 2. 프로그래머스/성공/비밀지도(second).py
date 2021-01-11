def solution(n, arr1, arr2):
    answer = []
    ans1=[]
    ans2=[]
    for i in arr1:
        temp=bin(i)[2:].zfill(n)
        ans1.append(list(map(int, temp)))

    
    for i in arr2:
        temp=bin(i)[2:].zfill(n)
        ans2.append(list(map(int, temp)))
    
    for i in range(n):
        temp=''
        for j in range(n):
            if ans2[i][j]==1 or ans1[i][j]==1:
                temp+='#'
            else:
                temp+=' '
        answer.append(temp)
    return answer
