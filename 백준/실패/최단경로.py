import sys

        v, e = map(int, input().split())
        k = int(input())

        INF = sys.maxsize

        come = [[] for i in range(v + 1)]  # 들어 오는 간선
        visit = [0 for i in range(v + 1)]  # 방문한 곳
        distance = [INF for i in range(v + 1)]  # 시작점에서 정점까지의 거리
        prev = [0 for i in range(v + 1)]  # 현재 정점으로 들어온 정점

        visit[k] = 1
        prev[k] = k
        distance[k] = 0

        for i in range(e):
            t = list(map(int, input().split()))
            come[t[0]].append((t[1], t[2]))

        print(come)
        while 1:  # 방문할 수 있는 곳이 없을 때 까지
            go = -1
            max_value = INF

            for i in range(len(come[k])):
                temp = come[k][i]
                if visit[temp[0]] and temp[1] < max_value:
                    max_value = i[1]
                    distance[temp[0]] = max(distance[k] + temp[1], distance[temp[0]])
                    go = temp[0]

            if go == -1:


#관련된 책을 읽어보고 논리 순서를 이해한 채로 풀어보려고 했다.
#하지만 dfs에서 다시 예쩐으로 돌아가는 것처럼 재귀가 필요했다.
#이 점에서 실패
