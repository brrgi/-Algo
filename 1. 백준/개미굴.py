import sys
sys.setrecursionlimit(10**8)
class Node():
    def __init__(self, key):
        self.key=key
        self.children={}

class Trie():
    def __init__(self):
        self.head=Node("")

    def firstAddress(self):
        curr_node = self.head
        return curr_node

    def insert(self, strings):      #strings는 문자열 리스트
        curr_node=self.head     #주소 넘기고

        for string in strings:
            if string not in curr_node.children:
                curr_node.children[string]=Node(string)

            curr_node=curr_node.children[string]



    def searchDfs(self, address, depth):
        curr_node=address
        result=('--'*depth)+curr_node.key+"\n"*(depth>=0)

        if curr_node.children=={}:
            return result

        else:
            curr_node.children=dict(sorted(curr_node.children.items()))

            for i in curr_node.children:
                result+=self.searchDfs(curr_node.children[i], depth + 1)

        return result

a=Trie()
n=int(input())

for i in range(n):
    t=list(map(str, input().split()))
    k=int(t[0])
    strings=[]
    for j in range(1, k+1):
        strings.append(t[j])
    a.insert(strings)
print(a.searchDfs(a.firstAddress(),-1).strip())