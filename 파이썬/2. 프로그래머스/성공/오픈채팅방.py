def solution(record):
    dicts = dict()
    result = []
    for i in record:
        k = list(map(str, i.split()))

        if k[0] == 'Enter':
            dicts[k[1]] = k[2]
            result.append([k[0], k[1]])
        elif k[0] == 'Leave':
            result.append([k[0], k[1]])
        else:
            dicts[k[1]] = k[2]

    answer = []
    for i in result:
        if i[0] == 'Enter':
            answer.append(dicts[i[1]] + "님이 들어왔습니다.")
        else:
            answer.append(dicts[i[1]] + "님이 나갔습니다.")


    return answer
