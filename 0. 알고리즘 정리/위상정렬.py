"""
주어진 그래프의 인접행렬을 바탕으로, 위상 정렬을 한다
입력: 그래프의 인접행렬
출력: 위상 정렬의 순서(같은 순서일 경우 아무거나 뽑음)
알고리즘
    1. 모든 정점의 진입 차수를 계산
    2. 진입 차수가 0인 정점을 스택에 삽입
    3. 위상 순서를 생성
"""
adj_mat = [[0, 0, 1, 1, 0, 0],
           [0, 0, 0, 1, 1, 0],
           [0, 0, 0, 1, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0, 0]]


def topological_sort(adj_mat):
    in_degrees = []
    stack = []
    answer = []

    for i in range(len(adj_mat)):
        temp = 0
        for col in range(len(adj_mat)):
            temp += adj_mat[col][i]
        in_degrees.append(temp)

    print("in_degrees: ", in_degrees)

    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            stack.append(i)

    print("stack: ", stack)

    while stack:
        node = stack.pop()
        answer.append(node)
        print("pop된 노드: ", node)

        for i in range(len(adj_mat[node])):
            if adj_mat[node][i] != 0:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    print("진입차수 0이 된 노드: ", i)
                    stack.append(i)

    print("answer: ", answer)


print(topological_sort(adj_mat))