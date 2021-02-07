a=int(input())
maps=[]
colors=['C', 'P', 'Z', 'Y']
dx=[1,-1]
dy=[1,-1]
for i in range(a):
    t=list(input())
    maps.append(t)


maxVal=1

for i in range(a):
    for j in range(a):
        for x in dx:
            newCol=j+x
            if 0<=newCol<a:
                # print("TL")
                maps[i][j],maps[i][newCol]=maps[i][newCol],maps[i][j]
                for e in range(a):  # 가로
                    initVal = 1
                    for r in range(a - 1):
                        if maps[e][r] == maps[e][r + 1]:
                            initVal += 1
                        else:
                            if initVal > maxVal:
                                maxVal = initVal
                            initVal = 1
                        if initVal > maxVal:
                            maxVal = initVal

                for e in range(a):  # 세로
                    initVal = 1
                    for r in range(a - 1):
                        if maps[r][e] == maps[r + 1][e]:
                            initVal += 1
                        else:
                            if initVal > maxVal:
                                maxVal = initVal
                            initVal = 1
                        if initVal > maxVal:
                            maxVal = initVal
                maps[i][j],maps[i][newCol]=maps[i][newCol],maps[i][j]

        for y in dx:
            newRow = i + y
            if 0 <= newRow < a:
                # print("TL")
                maps[i][j], maps[newRow][j] = maps[newRow][j], maps[i][j]
                for e in range(a - 1):  # 가로
                    initVal = 1
                    for r in range(a - 1):
                        if maps[e][r] == maps[e][r + 1]:
                            initVal += 1
                        else:
                            if initVal > maxVal:
                                maxVal = initVal
                            initVal = 1
                        if initVal > maxVal:
                            maxVal = initVal

                for e in range(a - 1):  # 세로
                    initVal = 1
                    for r in range(a - 1):
                        if maps[r][e] == maps[r + 1][e]:
                            initVal += 1
                        else:
                            if initVal > maxVal:
                                maxVal = initVal
                            initVal = 1
                        if initVal > maxVal:
                            maxVal = initVal
                maps[i][j], maps[newRow][j] = maps[newRow][j], maps[i][j]


print(maxVal)