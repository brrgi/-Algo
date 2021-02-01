num_student, num_compare = map(int, input().split())
graph_list = []
student_list = [[] for i in range(num_student + 1)]
indegree = [0 for i in range(num_student + 1)]
queue = []
result = []

#Graph Information

for i in range(num_compare):
    graph = list(map(int, input().split()))
    graph_list.append(graph)

#Node & Indegree Information

for [i, j] in graph_list:
    student_list[i].append(j)
    indegree[j] += 1

#Make First Queue

for i in range(1, num_student + 1):
    if indegree[i] == 0:
        queue.append(i)

#Make Topological Sort Loop

while queue:
    for i in queue:
        temp = i
        queue.remove(i)
        result.append(temp)
        for j in student_list[temp]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append(j)

for i in result:
    print(i, end=' ')