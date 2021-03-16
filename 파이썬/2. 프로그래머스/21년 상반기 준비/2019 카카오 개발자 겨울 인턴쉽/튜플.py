def solution(s):
    answer = []
    result=[set()]
    s=s[1:len(s)-1]
    temp = set()
    number=''
    prev='{'
    for word in s:
        if word=='{':
            temp=set()
            number=''
        elif word=='}':
            temp.add(int(number))
            number=''
            result.append(temp)
        elif word==',':
            if prev=='}':
                continue
            temp.add(int(number))
            number=''
        else:
            number+=word
        prev=word
    result.sort(key = lambda x : len(x))

    for i in range(len(result)-1):
        for j in result[i+1]-result[i]:
            answer.append(j)
    return answer

s="{{1,2,3},{2,1},{1,2,4,3},{2}}"
solution(s)