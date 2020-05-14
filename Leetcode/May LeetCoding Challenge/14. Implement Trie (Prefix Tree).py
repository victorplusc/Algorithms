"""
Implement Trie (Prefix Tree)
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""
class TrieNode:

    def __init__(self, val):
        self.val = val
        self.children = {}
        self.is_end = False

class Trie:
    
    # Time complexity: O(1)
    # Space complexity: O(1)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
        
    # Time complexity: O(N)
    # Space complexity: O(N)
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(c)    
            node = node.children[c]
        node.is_end = True
        
    # Time complexity: O(N)
    # Space complexity: O(1)
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True if node.is_end else False
    
    # Time complexity: O(N)
    # Space complexity: O(1)
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
