from collections import defaultdict
import sys
dic=defaultdict(int)
totalNumber=0
for line in sys.stdin:
    if line=='\n':
        break
    dic[line[:len(line)-1]]+=1
    totalNumber+=1
t=sorted(dic.items(), key=lambda x:x[0])
for item in t:
    if item=='false':
        break
    print("%s %.4f" %(item[0], item[1]*100/totalNumber))
