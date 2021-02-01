class Node():
    def __init__(self, key, data=None):
        self.key=key
        self.data=data
        self.children={}

class Trie():
    def __init__(self):
        self.head=Node(None)

    def insert(self, string):
        curr_node=self.head

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char]=Node(char)
            curr_node=curr_node.children[char]

        curr_node.data=string

    def search(self, string):
        curr_node=self.head
        for char in string:
            if char in curr_node.children:
                curr_node=curr_node.children[char]
            else:
                return False
        if (curr_node.data!=None):
            return True

n,m=map(int,input().split())
first=[]
result=0
new=Trie()
for i in range(n):
    temp=input()
    new.insert(temp)

for i in range(m):
    temp = input()
    if new.search(temp)==True:
        result+=1

print(result)

