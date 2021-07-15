import sys

input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
lis = [num[0]]


def bisect(number):
    left = 0
    right = len(lis) - 1
    result = 1000000

    while left <= right:
        mid = (left + right) // 2
        if lis[mid] >= number:  # 현재 가진 숫자 number가 더 작을 때
            if result > mid:    # 더 작은 숫자일 때마다 계속 저장    (result는 위치를 바꿀 index)
                result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

for i in range(1, n):
    if lis[-1] < num[i]:
        lis.append(num[i])
    else:
        lis[bisect(num[i])] = num[i]  # 값 바꾸기

print(len(lis))
