class TrieNode:

    def __init__(self, val) -> None:
        self.val = val
        self.child = [None] * 26
        self.word_end = False

class Trie:

    def __init__(self) -> None:
        self.root = TrieNode('')

    def insert(self, word):
        word = word.lower()
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if curr.child[idx] == None:
                node = TrieNode(c)
                curr.child[idx] = node
            curr = curr.child[idx]
        curr.word_end = True

    def search(self, word):
        curr = self.root
        word = word.lower()
        for c in word:
            idx = ord(c) - ord('a')
            if curr.child[idx] == None:
                return False
            curr = curr.child[idx]
        
        if curr.word_end:
            return True
            
if __name__ == '__main__':
    words = ['ant', 'and', 'anthony', 'do', 'tota']
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    print(trie.search('fdhjdf'))

            


        

