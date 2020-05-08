num=0
def next(stones, k, leng):
    global num
    first = 0
    # print("==============================")

    while 1:
        for i in range(k):
            if first + i < leng and stones[first + i] != 0:
                # print("df", first+i)
                stones[first + i] -= 1
                first += (1 + i)
                break
            elif first+i>=leng:
                # print(first+i)
                return stones
            elif i+1==k:
                # print(stones)
                return 0





def solution(stones, k):
    a = len(stones)
    global num
    while 1:
        stones = next(stones, k, a)
        if stones == 0:
            break
        else:
            num+=1

    answer = num
    print(num)
    return answer
