class Trie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insertWord(self, word: str):
        curr = self.root
        for letter in word:
            index = self._charToIndex(letter)
            if curr.children[index] is None:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isWord = True
        
        
    def searchWord(self, word: str):
        curr = self.root
        for letter in word:
            index = self._charToIndex(letter)
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True
            
        
    def _charToIndex(self, letter: str):
        return ord(letter.lower()) - ord('a')
    

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.isWord = False
        