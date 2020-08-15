n,l=map(int,input().split())

k=[list(map(int,input().split())) for i in range(n)]
number=0
# print(k)

for i in range(n):#가로
    visit=[0 for i in range(n)]
    visit[0]=1
    for j in range(n-1):
        if visit[j+1]!=0:
            continue
        if k[i][j]==k[i][j+1]:      #같을 때
            visit[j+1]=1
            continue
        elif k[i][j]-k[i][j+1]==1:  #떨어질 때
            temp=[]
            if j+l>=n:              #범위 오버
                break
            for q in range(1,l+1):
                temp.append(k[i][j+q])
            if len(set(temp))==1:
                for q in range(1, l + 1):
                    visit[j+q]=2
                # print(i,j,"보자", visit)
            else:
                break
        elif k[i][j]-k[i][j+1]==-1:  #오를 때
            # print(visit)

            temp=[]
            if j-(l-1) <0:           # 범위 오버
                break
            toggle=0
            for q in range(l):
                if visit[j-q]==2:
                    toggle=1
                    break
            if toggle==1:
                break
            for q in range(l):
                temp.append(k[i][j - q])
            if len(set(temp)) == 1:
                for q in range(l):
                    visit[j - q] = 1
                visit[j + 1] = 1
            else:
                break
        else:                        #1이상 차이가 나는 경우
            break
    if visit[-1] != 0:
        # print('0',visit)
        number += 1
    # else:
    #     print('1', visit)

# print(number)
for i in range(n):#세로
    visit = [0 for i in range(n)]
    visit[0] = 1
    for j in range(n - 1):
        if visit[j+1]!=0:
            continue
        if k[j][i] == k[j+1][i]:  # 같을 때
            visit[j + 1] = 1
            continue
        elif k[j][i] - k[j+1][i] == 1:  # 떨어질 때
            # print("보여줘",k[j][i], 'j랑 i', j, i)
            temp = []
            if j + l >= n:  # 범위 오버
                break
            for q in range(1, l + 1):
                temp.append(k[j+q][i])

            if len(set(temp)) == 1:
                for q in range(1, l + 1):
                    visit[j + q] = 2
            else:
                 break
        elif k[j][i] - k[j+1][i] == -1:  # 오를 때

            temp = []
            if j - (l - 1) < 0:  # 범위 오버
                break
            # print("여기", visit)
            toggle = 0
            for q in range(l):
                if visit[j-q]==2:
                    toggle = 1
                    break
            if toggle == 1:
                break
            for q in range(l):
                temp.append(k[j-q][i])
            if len(set(temp)) == 1:
                for q in range(l):
                    visit[j - q] = 2
                visit[j+1]=1
            else:
                break
        else:  # 1이상 차이가 나는 경우
            break
    if visit[-1] != 0:
        # print('0',visit)
        number += 1
    # else:
    #     print('1', visit)
print(number)
