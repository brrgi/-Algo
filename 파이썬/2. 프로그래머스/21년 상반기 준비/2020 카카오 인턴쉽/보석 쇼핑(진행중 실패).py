def solution(gems):
    answer = [0, 0]
    start = 0
    end = 1
    n = len(gems)
    resultLength = len(set(gems))

    while start < n:

        if len(set(gems[start:end])) < resultLength:
            if end == n:
                break
            end += 1
        else:
            if answer == [0, 0]:
                answer = [start, end]
            else:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            if answer != [0, 0] and (answer[1] - answer[0]) == resultLength:
                break
            start += 1
    answer = [answer[0] + 1, answer[1]]
    return answer