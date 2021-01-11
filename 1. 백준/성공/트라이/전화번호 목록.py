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
                if curr_node.data!=None:    #중간에 다른 값 있음 즉, 전치사
                    return False
                curr_node=curr_node.children[char]

        #마지막 도달
        if (curr_node.data!=None):
            return True

t=int(input())
for i in range(t):
    n=int(input())
    k=[]
    new=Trie()
    for i in range(n):
        temp=input()
        k.append(temp)
        new.insert(temp)

    a='YES'
    for i in k:
        if new.search(i)==False:
            a='NO'
            break
    print(a)
