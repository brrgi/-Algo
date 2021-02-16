from collections import deque

perfectPuzzle = '123456780'
puzzle = set()  # set    찾기 용
queue = deque()


def bfs(val):
    while 1:
        if perfectPuzzle in puzzle:
            return val
        val += 1
        leng = len(queue)
        if leng == 0:
            return -1

        for i in range(leng):
            data = queue.popleft()
            zeroIndex = data.index('0')
            x = data[zeroIndex]
            temp = '`'
            if zeroIndex == 0:
                make_string(data[:], temp, x, data[1])
                make_string(data[:], temp, x, data[3])

            elif zeroIndex == 1:
                make_string(data[:], temp, x, data[0])
                make_string(data[:], temp, x, data[2])
                make_string(data[:], temp, x, data[4])
            elif zeroIndex == 2:
                make_string(data[:], temp, x, data[1])
                make_string(data[:], temp, x, data[5])
            elif zeroIndex == 3:
                make_string(data[:], temp, x, data[0])
                make_string(data[:], temp, x, data[4])
                make_string(data[:], temp, x, data[6])
            elif zeroIndex == 4:
                make_string(data[:], temp, x, data[1])
                make_string(data[:], temp, x, data[3])
                make_string(data[:], temp, x, data[5])
                make_string(data[:], temp, x, data[7])
            elif zeroIndex == 5:
                make_string(data[:], temp, x, data[2])
                make_string(data[:], temp, x, data[4])
                make_string(data[:], temp, x, data[8])
            elif zeroIndex == 6:
                make_string(data[:], temp, x, data[3])
                make_string(data[:], temp, x, data[7])
            elif zeroIndex == 7:
                make_string(data[:], temp, x, data[4])
                make_string(data[:], temp, x, data[6])
                make_string(data[:], temp, x, data[8])
            elif zeroIndex == 8:
                make_string(data[:], temp, x, data[5])
                make_string(data[:], temp, x, data[7])


def make_string(dataTemp, temp, x, y):
    dataTemp = dataTemp.replace(x, temp)
    dataTemp = dataTemp.replace(y, x)
    dataTemp = dataTemp.replace(temp, y)
    if dataTemp not in puzzle:
        puzzle.add(dataTemp)
        queue.append(dataTemp)


first = ''
for i in range(3):
    t = list(map(str, input().split()))
    for j in range(3):
        first += t[j]
puzzle.add(first)
queue.append(first)

if perfectPuzzle in puzzle:
    print(0)
else:
    print(bfs(0))
