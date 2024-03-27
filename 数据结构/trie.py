from 基础.二阶差分 import Solution


class Trie:
    def __init__(self):
        self.children = dict()
        self.is_end = False

    def insert(self, word: str) -> None:
        p = self  
        for w in word:
            if w not in p.children:  
                p.children[w] = Trie()
            p = p.children[w]  
        p.is_end = True  

    def search(self, word: str) -> bool:
        p = self  
        for w in word:
            if w not in p.children:  
                return False
            p = p.children[w]  
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        p = self
        for w in prefix:
            if w not in p.children:
                return False
            p = p.children[w]
        return True

# 数组实现
class Trie:
    def __init__(self):
        self.is_end = False
        self.children = [None for _ in range(26)]

    def insert(self, word: str) -> None:
        p = self
        for c in word:
            idx = ord(c) - ord('a')
            if p.children[idx] == None:
                p.children[idx] = Trie()
            p = p.children[idx]
        p.is_end = True

    def search(self, word: str) -> bool:
        p = self
        for c in word:
            idx = ord(c) - ord('a')
            if not p.children[idx]:
                return False
            p = p.children[idx]
        return p.is_end

    def startsWith(self, prefix: str) -> bool:
        p = self
        for c in prefix:
            idx = ord(c) - ord('a')
            if not p.children[idx]:
                return False
            p = p.children[idx]
        return True