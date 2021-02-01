n=5000
def nums(number):
    how=0
    while number>1:
        if number%2==0:
            number=number//2
        else:
            how+=1
            number-=1
            number=number//2
    return how
def solution(n):
    ans = 0

    ans=nums(n)+1

    return ans

solution(n)
