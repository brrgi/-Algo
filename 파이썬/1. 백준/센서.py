from queue import PriorityQueue

n=int(input())
k=int(input())
sensor=[]
t=list(map(int,input().split()))
t=set(t)

for j in t:
    sensor.append(j)
sensor.sort()
first= sensor[-1] - sensor[0]
visit=[0 for i in range(len(sensor) - 1)]
q=PriorityQueue()

for i in range(len(sensor) - 1):
    q.put((100000 - (sensor[i + 1] - sensor[i]), (sensor[i + 1] - sensor[i])))       #우선순위, 값   -> 우선순위 작은게 먼저 나옴

for i in range(k - 1):
    if q.qsize()==0:
        break
    first-=q.get()[1]
print(first)