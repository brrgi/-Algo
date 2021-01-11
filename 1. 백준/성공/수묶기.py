n=int(input())
minus=[]
plus=[]
all=[]
for i in range(n):
    c=int(input())
    if c<=0:
        minus.append(c)
    else:
        plus.append(c)
minus.sort(reverse=True)
plus.sort()
while len(minus)>1:

    one=minus.pop()
    two=minus.pop()
    all.append(one*two)
all=all+minus

while len(plus)>1:

    one=plus[-1]
    two=plus[-2]
    if one+two<one*two:
        one=plus.pop()
        two=plus.pop()
        all.append(one*two)
    else:
        break

all=all+plus
# print(all)
print(sum(all))
