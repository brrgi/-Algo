class Node(object):
    """
    A node that consists of a trie.
    """

    def __init__(self, key, data=None , depth=None):
        self.key = key
        self.data = data
        self.depth = depth
        self.children = {}


class Trie(object):
    def __init__(self):
        self.head = Node(None)

    """
    트라이에 문자열을 삽입합니다.
    """

    def insert(self, string):
        curr_node = self.head
        now=0
        curr_node.depth=now
        for char in string:
            curr_node.depth=now
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]
            now+=1
            # string 의 마지막 글자 차례이면,
            # 노드의 data 필드에 저장하려는 문자열 전체를 저장한다.
        curr_node.depth = now
        curr_node.data = string

    """
    주어진 단어 string이 트라이에 존재하는지 여부를 반환합니다.
    """

    def search(self, string):
        curr_node = self.head
        how=0
        mid=0
        for char in string:
            if len(curr_node.children)!=1:
                how=curr_node.depth
            if curr_node.data!=None:
                mid=curr_node.depth
            if char in curr_node.children:
                curr_node = curr_node.children[char]


        # string의 마지막 글자에 다달았을 때,
        # curr_node 에 data 가 있다면 string이 트라이에 존재하는 것!
        if (curr_node.data != None):
            if mid==0:
                if len(curr_node.children)!=0:
                    mid=curr_node.depth-1
                else:
                    mid=how
            else:
                if len(curr_node.children)!=0:
                    mid = curr_node.depth - 1

        return mid+1

words=['ab', 'abc','abcd','abcef','abcefg']
def solution(words):
    answer = 0
    a=Trie()
    for word in words:
        a.insert(word)
    for word in words:
        answer+=a.search(word)
    return answer
solution(words)
