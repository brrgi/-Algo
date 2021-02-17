from collections import deque
perfectPuzzle = '123456780'
puzzle = set()      #set    찾기 용
queue=deque()

# q=a[3]
# w=a[4]
# temp='`'
# a=a.replace(q,temp)
# a=a.replace(w, q)
# a=a.replace(temp,w)

def bfs(str, val):
    while 1:
        if perfectPuzzle in puzzle:
            return val
        val += 1
        leng = len(queue)
        if leng == 0:
            return -1

        for i in range(leng):
            data=queue.popleft()
            dataTemp=data[:]
            zeroIndex=data.index('0')
            if zeroIndex==0:
                x=dataTemp[zeroIndex]
                y=dataTemp[1]
                temp='`'
                dataTemp=dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp=data[:]
                y=dataTemp[3]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

            elif zeroIndex==1:
                x = dataTemp[zeroIndex]
                y = dataTemp[0]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[2]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[4]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 2:
                x = dataTemp[zeroIndex]
                y = dataTemp[1]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[5]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 3:
                x = dataTemp[zeroIndex]
                y = dataTemp[0]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[4]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[6]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 4:
                x = dataTemp[zeroIndex]
                y = dataTemp[1]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[3]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[5]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[7]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 5:
                x = dataTemp[zeroIndex]
                y = dataTemp[2]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[4]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[8]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 6:
                x = dataTemp[zeroIndex]
                y = dataTemp[3]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[7]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 7:
                x = dataTemp[zeroIndex]
                y = dataTemp[4]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[6]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[8]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)
            elif zeroIndex == 8:
                x = dataTemp[zeroIndex]
                y = dataTemp[5]
                temp = '`'
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

                dataTemp = data[:]
                y = dataTemp[7]
                dataTemp = dataTemp.replace(x, temp)
                dataTemp = dataTemp.replace(y, x)
                dataTemp = dataTemp.replace(temp, y)
                if dataTemp not in puzzle:
                    puzzle.add(dataTemp)
                    queue.append(dataTemp)

first=''
for i in range(3):
    t=list(map(str, input().split()))
    for j in range(3):
        first+=t[j]
puzzle.add(first)
queue.append(first)

if perfectPuzzle in puzzle:
    print(0)
else:
    print(bfs(first , 0))