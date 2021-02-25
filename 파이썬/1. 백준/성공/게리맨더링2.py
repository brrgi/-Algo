n = int(input())


def calculate(x, y, d1, d2):
    newMap = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    a = 0
    for i in range(d1 + 1):
        newMap[x + i][y - i] = 5
        a+=1
    for i in range(d2 + 1):
        newMap[x + i][y + i] = 5
        a+=1
    for i in range(d2 + 1):
        newMap[x + d1 + i][y - d1 + i] = 5
        a += 1
    for i in range(d1 + 1):
        newMap[x + d2 + i][y + d2 - i] = 5
        a += 1
    for i in range(1, n+1):
        if newMap[i].count(5)>=2:
            firstIndex=newMap[i].index(5)
            newMap[i][firstIndex]=0
            secondIndex = newMap[i].index(5)
            newMap[i][firstIndex]=5
            for j in range(firstIndex+1, secondIndex):
                newMap[i][j]=5
    # for i in newMap:
    #     print(i)
    # print("시작", x, y, d1, d2)
    first = 0
    second = 0
    third = 0
    fourth = 0
    fifth = 0
    for i in range(1, x + d1):
        for j in range(1, y + 1):
            if newMap[i][j] == 5:
                break
            # print("1임", i, j)
            first += maps[i][j]
    for i in range(1, x + d2 +1):
        for j in range(y + 1, n + 1):
            if newMap[i][j] == 5:
                continue
            # print("2임", i, j)
            second += maps[i][j]
    for i in range(x + d1, n + 1):
        for j in range(1, y - d1 + d2):
            if newMap[i][j] == 5:
                break
            # print("3임", i, j)
            third += maps[i][j]
    for i in range(x + d2+1, n + 1):
        for j in range(y - d1 + d2, n + 1):
            if newMap[i][j] == 5:
                continue
            # print("4임", i, j)
            fourth += maps[i][j]

    for map in maps:
        fifth += sum(map)
    fifth -= first + second + third + fourth

    # print(first, second, third, fourth, fifth)
    # print(max(first, second, third, fourth, fifth) - min(first, second, third, fourth, fifth))
    return max(first, second, third, fourth, fifth) - min(first, second, third, fourth, fifth)


maps = [[0] * (n + 1)] + [[0] + list(map(int, input().split())) for _ in range(n)]
result = 1000000
for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, n + 1):
            for d2 in range(1, n + 1):

                if x + d1 + d2 > n:
                    continue
                if y - d1 < 1:
                    continue
                if y + d2 > n:
                    continue

                result = min(result, calculate(x, y, d1, d2))

print(result)
