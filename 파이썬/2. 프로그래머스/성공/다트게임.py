def trans(a):
    one=0
    two=0
    three=0
    score=[]
    bonus=[]
    option=[[] for i in range(3)]
    options=[-1, -1, -1]
    
    #bonus의 위치
    for i in range(len(a)):
        if a[i]=='S' or a[i]=='D' or a[i]=='T':
            if one==0:
                one=i
            elif two==0:
                two=i
            else:
                three=i
            bonus.append(a[i])
    print("one, two, three",one, two, three)
    print("bonus",bonus)
    for i in range(len(a)):
        if a[i]=='*' or a[i]=='#':
            if one<i<two:
                option[0].append(a[i])
                options[0]=i
            elif two<i<three:
                option[1].append(a[i])
                options[1]=i
            else:
                option[2].append(a[i])
                options[2]=i
    print(option)
    print(options)
    for i in range(3):
        if i==0:
            score.append(int(a[:one]))
        if i==1:
            if options[0]==-1:
                score.append(int(a[one+1:two]))
            else:
                score.append(int(a[one+2:two]))
        if i==2:
            if options[1]==-1:
                score.append(int(a[two+1:three]))
            else:
                score.append(int(a[two+2:three]))
    print(score)
    
    for i in range(3):
        if bonus[i]=='S':
            score[i]=score[i]**1
        elif bonus[i]=='D':
            score[i]=score[i]**2
        else:
            score[i]=score[i]**3
    print(score)
    

    if option[0]!=[]:
        if option[0][0]=='*':
            score[0]*=2
    if option[1]!=[]:
        if option[1][0]=='*':
            score[1]*=2
            score[0]*=2
    if option[2]!=[]:
        if option[2][0]=='*':
            score[1]*=2
            score[2]*=2
    for i in range(3):
        if option[i]!=[] and option[i][0]=='#':
            score[i]*=-1
    sum=0
    for i in range(3):
        sum+=score[i]
    return sum
def solution(dartResult):
    k=trans(dartResult)
    answer = k
    return answer
