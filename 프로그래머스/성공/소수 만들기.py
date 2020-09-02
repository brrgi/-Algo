#50C3 * 1000 =약 2천 5백만

from itertools import combinations
nums=[1,2,7,6,4]

def plus(one):
    result=0
    for i in one:
        result+=i
    return result

def sosu(number):
    toggle=0
    for i in range(2, number):
        if number%i==0:
            toggle=1
            break

    return toggle

def solution(nums):
    answer = 0

    all=list(combinations(nums, 3))

    for i in all:
        if sosu(plus(i))==0:
            answer+=1


    return answer

print(solution(nums))
