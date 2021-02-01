#55-50+40
#55-50+40-10+60
#10-40-50-60

k=input()
trigger=0
string=[]
one=''
for i in range(len(k)):
    if '-'==k[i] or '+'==k[i]:
        string.append(one)
        string.append(k[i])
        one=''
        continue
    else:
        one=one+k[i]
string.append(one)
#print(string)
sum=0
trigger=0
for i in string:
    if i.isdigit()==1:
        if trigger==0:
            sum+=int(i)
        else:
            sum-=int(i)
    else:
        if i=='-':
            trigger=1
print(sum)
