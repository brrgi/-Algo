import sys

sys.setrecursionlimit(10 ** 8)


class Node():
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie():
    def __init__(self):
        self.head = Node(None)

    def first(self):
        curr_node = self.head
        return curr_node

    def insert(self, string):
        curr_node = self.head  # 주소 넘기고

        for char in string:
            if char not in curr_node.children:
                curr_node.children[char] = Node(char)

            curr_node = curr_node.children[char]

        curr_node.data = string

    def search(self, char, address):
        curr_node=address
        if char in curr_node.children:
            curr_node = curr_node.children[char]
            return curr_node
        else:
            return False



dir = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 11)]


def dfs(row, col, now, address, visit):

    visit[row][col] = 1
    print("멈", row, col, now)
    if now in wordSet:      #생각해보니 sum summmmmm이 있는 경우 sum만을 추출하고 뒤에 있는 summmmmm을 검색할 수 없게 짰다. ㅜㅜ
        newSet.add(now)
        return True
    if t.search(maps[row][col], address)==False:
        return True
    else:

        for i in dir:
            newRow = row + i[0]
            newCol = col + i[1]
            if (0 <= newRow < 4 and 0 <= newCol < 4 and visit[newRow][newCol] == 0):
                visit[newRow][newCol] = 1
                dfs(newRow, newCol, now + maps[newRow][newCol], t.search(maps[row][col], address), visit)
                visit[newRow][newCol] = 0


t = Trie()
w = int(input())
wordSet=set()
for i in range(w):
    word = input()
    wordSet.add(word)
    t.insert(word)
input()

b = int(input())
for i in range(b - 1):
    newSet=set()
    maps = []
    visit = [[0 for _ in range(4)] for _ in range(4)]
    for _ in range(4):
        maps.append(list(input()))
    for q in range(4):
        for e in range(4):
            dfs(q, e, maps[q][e], t.first(), visit)
    print(newSet)
    input()
newSet=set()
maps = []
result = []
visit = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(4):
    maps.append(list(input()))
for q in range(4):
    for e in range(4):
        temp = dfs(q, e, maps[q][e], t.first(), visit)
        if temp != False:
            result.append(temp)
print(newSet)
