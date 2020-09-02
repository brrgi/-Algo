from collections import deque
def solution(d, budget):
    answer = 0
    first=deque()
    queue=deque()
    d.sort()
    for i in d:
        queue.append(i)
    
    if budget!=0:
        while queue:
            if budget==0:
                break
            if budget<0:
                answer-=1
                break

            if queue!=first:
                answer+=1
                budget=budget-queue[0]
                queue.popleft()
    if queue==first and budget<0:
        answer-=1
    return answer
