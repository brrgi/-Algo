t=input()
length1=len(t)
tt=input()
length2=len(tt)

i=0
cnt=0
while i<length1-(length2-1):
    if tt==t[i:i+length2]:
        cnt+=1
        i+=length2
    else:
        i+=1
print(cnt)
