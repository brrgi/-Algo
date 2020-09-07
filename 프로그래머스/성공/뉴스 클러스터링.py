str1='aa1+aa2'
str2='AAAA12'
def solution(str1, str2):
    answer = 0
    str1=str1.upper()
    str2=str2.upper()
    A=dict()
    B=dict()
    new=dict()
    newLength=0
    print(str1, str2)
    for i in range(len(str1)-1):
        if ord(str1[i])<65 or ord(str1[i])>90 or ord(str1[i+1])<65 or ord(str1[i+1])>90:
            continue
        if str1[i]+str1[i+1] not in A.keys():
            A[str1[i]+str1[i+1]]=1
        else:
            A[str1[i]+str1[i+1]]+=1

        if str1[i]+str1[i+1] not in new.keys():
            new[str1[i]+str1[i+1]]=1
        else:
            new[str1[i]+str1[i+1]]+=1

    for i in range(len(str2)-1):
        if ord(str2[i])<65 or ord(str2[i])>90 or ord(str2[i+1])<65 or ord(str2[i+1])>90:
            continue
        if str2[i]+str2[i+1] not in B.keys():
            B[str2[i]+str2[i+1]]=1
        else:
            B[str2[i]+str2[i+1]]+=1

    result = 0
    for i in B:
        if i not in new:
            new[i]=B[i]
        else:
            if new[i]<B[i]:
                result+=new[i]
                new[i]=B[i]
            else:
                result+=B[i]

    for i in new:
        newLength+=new[i]
    if len(new)==0:
        return 65536
    ans=result/newLength
    ans*=65536
    ans=int(ans)
    answer=ans
    return answer
solution(str1, str2)
