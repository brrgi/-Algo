alph1=[0 for i in range(26)]
alph2=[0 for i in range(26)]

a=input()
b=input()
for i in a:
    alph1[ord(i)-97]+=1
for i in b:
    alph2[ord(i)-97]+=1

num=0
for i in range(26):
    num+=abs(alph1[i]-alph2[i])
print(num)
