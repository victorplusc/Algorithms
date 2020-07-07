"""
211. Add and Search Word - Data structure design
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
"""
class WordDictionary:

    # Time complexity: O(1)
    # Space complexity: O(1)
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    # Time complexity: O(N)
    # Space complexity: O(N)
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = True

    # Time complexity: O(N)
    # Space complexity: O(N)
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def search_in_node(word, node):
            for i, c in enumerate(word):
                if c not in node:
                    if c == ".":
                        for x in node:
                            if x != "$" and search_in_node(word[i+1:], node[x]):
                                return True
                    return False
                else:
                    node = node[c]
            return "$" in node
        return search_in_node(word, self.trie)        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
