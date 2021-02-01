def finding(words, query, now, where):
    k=1
    now1=now-1
    now2=now+1
    while 0<=now1:
        if words[now1][:where]==query[:where] and len(words[now1])==len(query):
            k+=1
            now1-=1
        else:
            break
    while now2<len(words):
        if words[now2][:where]==query[:where] and len(words[now2])==len(query):
            k+=1
            now2+=1
        else:
            break
    return k
            

def solution(words, queries):
    answer = []
    reverseWords=[]
    reverseQueries=[]
    words.sort()
    wordss=[[] for i in range(100001)]
    for i in words:
        wordss[len(i)].append(i)
        
    for i in words:
        reverseWords.append(i[::-1])
    reverseWords.sort()
    reverseWordss=[[] for i in range(100001)]
    for i in reverseWords:
        reverseWordss[len(i)].append(i)
    for i in queries:
        toggle=0
        if i[0]=='?':   #앞에 ??먼저 나오는 것
            ii=list(i[::-1])
            i=i[::-1]
            where=ii.index('?')
            
            start=0
            end=len(wordss[len(i)])-1
            while start<=end:
                mid=(start+end)//2

                if reverseWordss[len(i)][mid][:where]==i[:where]:
                    if len(reverseWordss[len(i)][mid])==len(i):
                        answer.append(finding(reverseWordss[len(i)], i, mid, where))
                        toggle=1
                        break
                    elif len(reverseWordss[len(i)][mid])<len(i):
                        start=mid+1
                    else:
                        end=mid-1
                elif reverseWordss[len(i)][mid][:where]>i[:where]:
                    start=mid+1
                else:
                    end=mid-1
        else:   #정상
            ii=list(i)
            where=ii.index('?')
            
            start=0
            end=len(wordss[len(i)])-1
            while start<=end:
                mid=(start+end)//2

                if wordss[len(i)][mid][:where]==i[:where]:
                    if len(wordss[len(i)][mid])==len(i):
                        answer.append(finding(wordss[len(i)], i, mid, where))
                        toggle=1
                        break
                    elif len(wordss[len(i)][mid])<len(i):
                        start=mid+1
                    else:
                        end=mid-1
                elif wordss[len(i)][mid][:where]>i[:where]:
                    start=mid+1
                else:
                    end=mid-1

        if toggle==0:
            answer.append(0)
                
        
    
    return answer
