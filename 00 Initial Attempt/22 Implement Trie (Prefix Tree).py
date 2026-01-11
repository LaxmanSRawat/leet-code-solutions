from collections import deque
class Node(object):
    def __init__(self,val):
        self.val = val
        self.childNodes={}

class Trie:

    def __init__(self):
        self.root = Node(None)
        

    def insert(self, word: str) -> None:
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.childNodes:
                newNode = Node(letter)
                currentNode.childNodes[letter] = newNode
                currentNode = newNode
            else:
                currentNode = currentNode.childNodes[letter]
        currentNode.childNodes[1] = Node(None) # word end indicator 
    
    def printBfs(self):
        q = deque()
        q.append(self.root)
        
        while(q):
            current_level = []
            for _ in range(len(q)):
                currentNode = q.popleft()
                current_level.append(currentNode.val)
                for i in currentNode.childNodes:
                    q.append(currentNode.childNodes[i])
            print(current_level)



    def search(self, word: str) -> bool:
        currentNode = self.root
        for letter in word:
            if letter not in currentNode.childNodes:
                return False
            currentNode = currentNode.childNodes[letter]
        if 1 in currentNode.childNodes:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for letter in prefix:
            if letter not in currentNode.childNodes:
                return False
            currentNode = currentNode.childNodes[letter]
        return True
        


# Your Trie object will be instantiated and called as such:
trie = Trie()
trie.insert("apple")
# print(trie.root.childNodes["p"].val)
trie.printBfs()
print(trie.search("apple"))    #return True
print(trie.search("app"))     #return False
print(trie.startsWith("app")) # return True
trie.insert("app")
print(trie.search("app"))    # return True