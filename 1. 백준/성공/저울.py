n = int(input())
k = list(map(int, input().split()))
k.sort()
num = 1
for i in range(n):
    if num < k[i]:
        break
    num += k[i]
print(num)

#실패코드
# import sys
# input=sys.stdin.readline
# 
# a=int(input())
# k=list(map(int, input().split()))
# k.sort(reverse=True)
# 
# i=0
# while i<=sum(k):
#     i+=1
#     num=i
#     for j in k:
#         if num-j>=0:
#             num=num-j
#     if num!=0:
#         print(i)
#         break
