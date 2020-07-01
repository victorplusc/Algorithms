"""
212. Word Search II
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""
# Time complexity: O(M*(4*3**(L-1)))
# Space complexity: O(N)
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"
        
        trie = {}
        for word in words:
            node = trie
            for c in word:
                node = node.setdefault(c, {})
            node[WORD_KEY] = word
        
        def backtrack(y, x, trie):
            letter = board[y][x]
            curr_node = trie[letter]
            
            word_match = curr_node.pop(WORD_KEY, False)
            if word_match:
                found.append(word_match)
            
            board[y][x] = "X"
            
            for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                r, c = dy+y, dx+x
                if r < 0 or r >= n or c < 0 or c >= m: continue
                if board[r][c] not in curr_node:
                    continue
                backtrack(r, c, curr_node)
            board[y][x] = letter
            if not curr_node:
                trie.pop(letter)
        
        n, m = len(board), len(board[0])
        found = []
        for i in range(n):
            for j in range(m):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        
        return found
