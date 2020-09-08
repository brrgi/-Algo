food_times=[3,1,2]
k=5
def solution(food_times, k):
    all=0
    kk=k
    answer = 0
    newOne = []
    for i in enumerate(food_times):
        newOne.append(list(i))

    newOne = sorted(newOne, key=lambda x:x[1])

    while 1:
        toggle=0
        if k-len(newOne)<0:
            break
        for i in range(len(newOne)):
            if newOne[i][1]==0:
                continue
            else:
                newOne[i][1] -= 1
                all+=1
                if newOne[i][1]!=0:
                    toggle+=1
                k-=1
        if toggle==0:
            return -1

    newOne=sorted(newOne, key=lambda x:x[0])
    while k>=-1:
        toggle=0
        for i in range(len(newOne)):
            if newOne[i][1]!=0:
                k-=1
                newOne[i][1]-=1
                if newOne[i][1]!=0:
                    toggle+=1
                all+=1
            if k==-1:
                answer=i+1
                break
        if toggle==0:
            break
    if k==0:
        return -1
    return answer

print(solution(food_times, k))
