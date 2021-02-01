n=16
stations=[9]
w=2

def value(number, divValue):
    ans=0
    while number>0:
        if number-divValue>=0:
            number=number-divValue
            ans+=1
        else:
            ans+=1
            break
    return ans
def solution(n, stations, w):
    answer = 0
    new=[]
    now=1
    for i in stations:
        new.append((i-w)-now)
        now=(i+w)+1
    if n>=now:
        new.append(n-now+1)
    divValue=1+2*w
    for i in new:
        answer+=value(i, divValue)

    return answer

solution(n, stations, w)
