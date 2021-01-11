skill="CBD"
skill_trees=["BACDE", "CBADF", "AECB", "BDA"]


def solution(skill, skill_trees):
    answer = 0
    now = 1

    visit=[0 for i in range(26)]
    t=1
    for i in skill:
        visit[ord(i)-65]=t
        t+=1

    for i in skill_trees:
        now=1
        toggle=0
        for j in i:
            if visit[ord(j)-65]==0:
                continue
            elif visit[ord(j)-65]==now:
                now+=1
                continue
            else:
                toggle=1
                break
        if toggle==0:
            answer+=1

    return answer

print(solution(skill, skill_trees))
