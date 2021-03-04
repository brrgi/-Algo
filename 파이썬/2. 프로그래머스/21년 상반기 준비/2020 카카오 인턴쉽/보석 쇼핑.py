def solution(gems):
    answer = [0, 0]
    start = 0
    end = 1
    n = len(gems)
    check={}
    for ge in set(gems):
        check[ge]=0

    resultLength = len(set(gems))

    check[gems[0]]=1
    currentPick=1

    while start < n:
        if currentPick < resultLength:
            if end == n:
                break
            if check[gems[end]] == 0:
                currentPick += 1
            check[gems[end]] += 1
            end += 1
        else:
            if answer == [0, 0]:
                answer = [start, end]
            else:
                if end - start < answer[1] - answer[0]:
                    answer = [start, end]
            if answer != [0, 0] and (answer[1] - answer[0]) == resultLength:    #중간에 만족되면 끝
                break

            check[gems[start]] -= 1
            if check[gems[start]] == 0:
                currentPick -= 1
            start += 1

    answer = [answer[0] + 1, answer[1]]
    return answer


gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
solution(gems)