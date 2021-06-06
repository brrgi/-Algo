import heapq

a = int(input())
left = []
right = []

for i in range(a):
    number = int(input())
    if (i + 1) % 2 == 1:
        heapq.heappush(right, number)
    else:
        heapq.heappush(left, -number)

    if left != []:
        lValue = -left[0]
        rValue = right[0]
        if lValue > rValue:
            heapq.heappush(left, -heapq.heappop(right))
            heapq.heappush(right, -heapq.heappop(left))

    if (i + 1) % 2 == 1:
        print(right[0])
    else:
        print(min(-left[0], right[0]))
