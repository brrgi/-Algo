from collections import deque
def solution(cacheSize, cities):
    a=[]
    ai=0
    hit=1
    miss=5
    for i in range(len(cities)):
        cities[i]=cities[i].lower()
    if cacheSize==0:
        ai+=len(cities)*5
    else:
        for i in cities:
            if len(a)<cacheSize:
                if i in a:
                    a.pop(a.index(i))
                    a.append(i)
                    ai+=hit
                else:
                    a.append(i)
                    ai+=miss
            else:
                if i in a:
                    a.pop(a.index(i))
                    a.append(i)
                    ai+=hit
                else:
                    a.pop(0)
                    a.append(i)
                    ai+=miss

    answer = ai
    return answer
