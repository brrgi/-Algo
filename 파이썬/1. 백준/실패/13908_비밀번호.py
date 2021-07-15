import sys
sys.setrecursionlimit(10**8)
n,m=map(int, input().split())
know=set(map(int, input().split()))
masking=0
for i in know:
    masking|=1<<i

result=[]

def brute(nums):
    if len(nums[1])==n:
        if nums[0]==masking:
            result.append(nums)
        return

    for i in range(10):
        if i in know:
            brute((nums[0]|1<<i,nums[1]+str(i)))
        else:
            brute((nums[0],nums[1]+str(i)))

brute((0,''))
print(len(result))