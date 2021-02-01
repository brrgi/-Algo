n=3
words=['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']

def solution(n, words):
    answer = []
    i=0
    prev=[]
    prev.append(words[0])
    toggle=0
    while i<len(words)-1:
        if words[i][-1]==words[i+1][0]:
            if words[i+1] not in prev:
                prev.append(words[i])
                i+=1
            else:
                i+=2
                toggle = 1
                break
        else:
            i+=2
            toggle = 1
            break
    if toggle==0:
        i+=1
        return [0,0]
    value=i%n
    if value ==0:
        value=n
        value1=i//n
    else:
        value1=i//n+1
    answer=[value,value1]
    return answer

solution(n, words)
